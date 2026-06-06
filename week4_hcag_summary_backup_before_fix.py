#!/usr/bin/env python3
"""
Week 4 HCAG-style hierarchical architectural recovery for Group 4 Lucene Codecs.


Reads ARC cluster output, maps cluster entities to Java source files, performs:
1) Leaf summaries from raw Java files.
2) Directory/branch summaries from child summaries only.
3) Cluster architectural title + high-level summary from summaries only.


Outputs are saved under output/week4_hcag_arch_recovery by default.
"""


from __future__ import annotations


import argparse
import csv
import json
import os
import re
import sys
import time
from collections import defaultdict
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple


import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


try:
   from transformers import BitsAndBytesConfig
except Exception:  # pragma: no cover
   BitsAndBytesConfig = None




# -----------------------------
# Utility
# -----------------------------




def log(msg: str) -> None:
   print(msg, flush=True)




def safe_filename(value: str, max_len: int = 180) -> str:
   value = value.replace(os.sep, "_")
   value = value.replace("/", "_").replace("\\", "_")
   value = re.sub(r"[^A-Za-z0-9_.-]+", "_", value).strip("_")
   if not value:
       value = "item"
   return value[:max_len]




def normalize_entity_name(x: str) -> str:
   x = x.strip().strip('"').strip("'").strip(",")
   x = x.replace("/", ".").replace("\\", ".")
   if x.endswith(".class"):
       x = x[:-6]
   if x.endswith(".java"):
       x = x[:-5]
   x = x.replace("$", ".")
   while ".." in x:
       x = x.replace("..", ".")
   return x.strip(".")




def read_text(path: Path) -> str:
   return path.read_text(encoding="utf-8", errors="ignore")




def write_text(path: Path, text: str) -> None:
   path.parent.mkdir(parents=True, exist_ok=True)
   path.write_text(text, encoding="utf-8")




def truncate_middle(text: str, max_chars: int) -> str:
   if len(text) <= max_chars:
       return text
   keep_head = max_chars // 2
   keep_tail = max_chars - keep_head
   return (
       text[:keep_head]
       + "\n\n/* ... TRUNCATED FOR CONTEXT LIMIT ... */\n\n"
       + text[-keep_tail:]
   )




def parse_package(java_text: str) -> str:
   m = re.search(r"^\s*package\s+([A-Za-z0-9_.]+)\s*;", java_text, flags=re.MULTILINE)
   return m.group(1) if m else ""




# -----------------------------
# Cluster parsing and source mapping
# -----------------------------




def parse_cluster_rsf(path: Path) -> Dict[str, List[str]]:
   if not path.exists():
       raise FileNotFoundError(f"Cluster RSF not found: {path}")


   clusters: Dict[str, List[str]] = defaultdict(list)


   with path.open("r", encoding="utf-8", errors="ignore") as f:
       for line in f:
           raw = line.strip()
           if not raw or raw.startswith("#"):
               continue
           parts = raw.split()
           if len(parts) < 3:
               continue
           rel = parts[0].lower()
           if rel != "contain":
               continue


           # Standard ARCADE format: contain <cluster> <entity>
           cluster = parts[1]
           entity = parts[2]
           clusters[cluster].append(normalize_entity_name(entity))


   if not clusters:
       raise RuntimeError(f"No clusters found in {path}. Expected lines like: contain Cluster Entity")


   return dict(clusters)




def find_java_root(work_dir: Path, source_root_arg: Optional[str]) -> Path:
   if source_root_arg:
       root = Path(source_root_arg)
       if not root.exists():
           raise FileNotFoundError(f"Provided source root does not exist: {root}")
       return root


   candidates = [
       work_dir / "src" / "lucene",
       work_dir / "src",
       work_dir / "lucene",
       work_dir,
   ]


   for c in candidates:
       if c.exists() and any(c.rglob("*.java")):
           return c


   raise FileNotFoundError(
       "Could not find Java source files. Expected them under group4/src or pass --source-root."
   )




def discover_java_files(source_root: Path) -> Tuple[List[Path], Dict[str, Path]]:
   skip_parts = {".git", "target", "build", "out", ".gradle", "venv_arc", "venv_week4", "cache", "output"}
   java_files: List[Path] = []


   for p in source_root.rglob("*.java"):
       if any(part in skip_parts for part in p.parts):
           continue
       java_files.append(p)


   if not java_files:
       raise FileNotFoundError(f"No .java files found under {source_root}")


   index: Dict[str, Path] = {}


   for path in java_files:
       try:
           text = read_text(path)
       except Exception:
           text = ""


       package = parse_package(text)
       stem = path.stem
       rel_no_ext = path.relative_to(source_root).with_suffix("").as_posix().replace("/", ".")


       keys = set()
       keys.add(normalize_entity_name(stem))
       keys.add(normalize_entity_name(rel_no_ext))
       if package:
           keys.add(normalize_entity_name(f"{package}.{stem}"))


       # Also index suffix after common Java source roots when present
       rel_parts = path.relative_to(source_root).with_suffix("").parts
       for marker in ("java", "src"):
           if marker in rel_parts:
               idx = rel_parts.index(marker)
               suffix = ".".join(rel_parts[idx + 1 :])
               if suffix:
                   keys.add(normalize_entity_name(suffix))


       for key in keys:
           index.setdefault(key, path)


   return java_files, index




def match_entity_to_file(entity: str, index: Dict[str, Path]) -> Optional[Path]:
   e = normalize_entity_name(entity)
   if e in index:
       return index[e]


   # Try class basename.
   last = e.split(".")[-1]
   if last in index:
       return index[last]


   # Try suffix matching: package may differ by Lucene version/source root.
   suffix_matches = [(k, p) for k, p in index.items() if k.endswith("." + e) or e.endswith("." + k)]
   if suffix_matches:
       suffix_matches.sort(key=lambda kp: len(kp[0]))
       return suffix_matches[0][1]


   # Try inner-class outer name.
   if "." in last:
       outer = last.split(".")[0]
       if outer in index:
           return index[outer]


   return None




# -----------------------------
# Model and generation
# -----------------------------




def load_llm(model_name, hf_token=None, use_4bit=True):
   import torch
   from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig


   print(f"Loading model: {model_name}", flush=True)
   print("CUDA available:", torch.cuda.is_available(), flush=True)
   print("CUDA device count:", torch.cuda.device_count(), flush=True)


   if not torch.cuda.is_available():
       raise RuntimeError("CUDA is not available. Mixtral must run on GPU nodes.")


   gpu_count = torch.cuda.device_count()


   if gpu_count < 2 and "Mixtral" in model_name:
       raise RuntimeError("Mixtral requires 2 GPUs. Use #SBATCH --gres=gpu:a100:2")


   for i in range(gpu_count):
       print(f"GPU {i}: {torch.cuda.get_device_name(i)}", flush=True)


   tokenizer = AutoTokenizer.from_pretrained(
       model_name,
       token=hf_token,
       trust_remote_code=True,
       use_fast=True
   )


   if tokenizer.pad_token is None:
       tokenizer.pad_token = tokenizer.eos_token


   dtype = torch.bfloat16


   model_kwargs = {
       "token": hf_token,
       "trust_remote_code": True,
       "torch_dtype": dtype,
       "low_cpu_mem_usage": True,
   }


   if use_4bit:
       print("Loading Mixtral in 4-bit NF4 quantization.", flush=True)
       model_kwargs["quantization_config"] = BitsAndBytesConfig(
           load_in_4bit=True,
           bnb_4bit_quant_type="nf4",
           bnb_4bit_compute_dtype=dtype,
           bnb_4bit_use_double_quant=True,
       )


   if "Mixtral" in model_name:
       print("Using GPU-0-light manual 2-GPU device map for Mixtral.", flush=True)


       device_map = {
           "model.embed_tokens": 0,
           "model.norm": 1,
           "lm_head": 1,
       }


       # Mixtral-8x7B has 32 decoder layers.
       # Put fewer layers on GPU 0 because GPU 0 was filling first.
       for layer_idx in range(32):
           if layer_idx < 10:
               device_map[f"model.layers.{layer_idx}"] = 0
           else:
               device_map[f"model.layers.{layer_idx}"] = 1


       model_kwargs["device_map"] = device_map
       model_kwargs["max_memory"] = {
           0: "35GiB",
           1: "39GiB",
       }


   else:
       model_kwargs["device_map"] = "auto"
       model_kwargs["max_memory"] = {
           0: "38GiB",
       }


   model = AutoModelForCausalLM.from_pretrained(
       model_name,
       **model_kwargs
   )


   model.eval()


   if hasattr(model, "config"):
       model.config.use_cache = False


   print("Model loaded successfully.", flush=True)


   return tokenizer, model


def build_chat_prompt(tokenizer, system_prompt: str, user_prompt: str) -> str:
   messages = [
       {"role": "system", "content": system_prompt},
       {"role": "user", "content": user_prompt},
   ]
   if hasattr(tokenizer, "apply_chat_template") and tokenizer.chat_template:
       return tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
   return f"SYSTEM:\n{system_prompt}\n\nUSER:\n{user_prompt}\n\nASSISTANT:\n"




def generate_text(
   tokenizer,
   model,
   system_prompt: str,
   user_prompt: str,
   max_new_tokens: int,
   max_input_tokens: int,
) -> str:
   prompt = build_chat_prompt(tokenizer, system_prompt, user_prompt)
   inputs = tokenizer(
       prompt,
       return_tensors="pt",
       truncation=True,
       max_length=max_input_tokens,
       padding=False,
   )


   first_device = next(model.parameters()).device
   inputs = {k: v.to(first_device) for k, v in inputs.items()}


   generation_temperature = float(os.environ.get("GENERATION_TEMPERATURE", "0.0"))
   generation_top_p = float(os.environ.get("GENERATION_TOP_P", "0.9"))
   do_sample = generation_temperature > 0.0


   generation_kwargs = dict(
       **inputs,
       max_new_tokens=max_new_tokens,
       do_sample=do_sample,
       pad_token_id=tokenizer.eos_token_id,
       eos_token_id=tokenizer.eos_token_id,
       use_cache=False,
   )


   if do_sample:
       generation_kwargs["temperature"] = generation_temperature
       generation_kwargs["top_p"] = generation_top_p


   with torch.no_grad():
       outputs = model.generate(**generation_kwargs)


   new_tokens = outputs[0][inputs["input_ids"].shape[1] :]
   text = tokenizer.decode(new_tokens, skip_special_tokens=True).strip()


   del inputs, outputs, new_tokens
   if torch.cuda.is_available():
       torch.cuda.empty_cache()


   return text




# -----------------------------
# Prompts
# -----------------------------




SYSTEM_PROMPT = (
   "You are a software architecture recovery assistant. "
   "You analyze Java source code and architectural summaries precisely. "
   "Do not invent behavior not supported by the provided input. "
   "Write concise, technical, report-ready summaries."
)




def leaf_prompt(entity: str, rel_path: str, source: str) -> str:
   return f"""
You are processing a leaf node in a hierarchical architectural recovery pipeline.


Entity: {entity}
Relative file path: {rel_path}


Analyze the raw Java source code below and produce a semantic summary with these headings:


1. File title
2. Key functionality
3. Core logic
4. Inputs and outputs
5. Internal and external dependencies
6. Architectural role inside the cluster
7. Important classes/methods


Use only the source code provided. Be concise but specific.


```java
{source}
```
""".strip()




def directory_prompt(dir_path: str, child_summaries: str) -> str:
   return f"""
You are processing a branch/directory node in a hierarchical architectural recovery pipeline.


Directory path: {dir_path}


Use ONLY the child summaries below. Do not assume access to raw source code.


Generate:
1. Directory/module title
2. High-level descriptive summary
3. Main responsibilities
4. How the child components interact
5. Architectural role within the cluster


Child summaries:


{child_summaries}
""".strip()




def cluster_prompt(cluster_id: str, summaries: str) -> str:
   return f"""
You are generating the final architectural recovery output for one software cluster.


Cluster ID: {cluster_id}


Use ONLY the file and directory summaries below.


Return exactly this format:


TITLE:


<short architectural title>


DESCRIPTION:


<under 150 words. Include components and interactions, quality attributes such as maintainability/scalability/security if relevant, and technologies/languages/tools used.>


Summaries:


{summaries}
""".strip()




# -----------------------------
# Hierarchical summarization
# -----------------------------




def summarize_leaf(
   tokenizer,
   model,
   entity: str,
   source_file: Path,
   source_root: Path,
   out_path: Path,
   max_source_chars: int,
   max_input_tokens: int,
   force: bool,
) -> str:
   if out_path.exists() and not force:
       return read_text(out_path)


   rel = source_file.relative_to(source_root).as_posix()
   source = truncate_middle(read_text(source_file), max_source_chars)
   prompt = leaf_prompt(entity, rel, source)
   summary = generate_text(
       tokenizer,
       model,
       SYSTEM_PROMPT,
       prompt,
       max_new_tokens=550,
       max_input_tokens=max_input_tokens,
   )
   write_text(out_path, summary)
   return summary




def summarize_directory(
   tokenizer,
   model,
   dir_label: str,
   child_text: str,
   out_path: Path,
   max_summary_chars: int,
   max_input_tokens: int,
   force: bool,
) -> str:
   if out_path.exists() and not force:
       return read_text(out_path)


   prompt = directory_prompt(dir_label, truncate_middle(child_text, max_summary_chars))
   summary = generate_text(
       tokenizer,
       model,
       SYSTEM_PROMPT,
       prompt,
       max_new_tokens=650,
       max_input_tokens=max_input_tokens,
   )
   write_text(out_path, summary)
   return summary




def summarize_cluster(
   tokenizer,
   model,
   cluster_id: str,
   all_summaries: str,
   out_path: Path,
   max_summary_chars: int,
   max_input_tokens: int,
   force: bool,
) -> str:
   if out_path.exists() and not force:
       return read_text(out_path)


   prompt = cluster_prompt(cluster_id, truncate_middle(all_summaries, max_summary_chars))
   summary = generate_text(
       tokenizer,
       model,
       SYSTEM_PROMPT,
       prompt,
       max_new_tokens=900,
       max_input_tokens=max_input_tokens,
   )
   write_text(out_path, summary)
   return summary




def collect_directory_summaries(
   tokenizer,
   model,
   cluster_id: str,
   file_summary_by_rel: Dict[str, str],
   dir_out_base: Path,
   max_summary_chars: int,
   max_input_tokens: int,
   force: bool,
) -> Dict[str, str]:
   """Bottom-up directory summaries using only child summaries."""
   dirs = set()
   for rel in file_summary_by_rel:
       p = Path(rel).parent
       while str(p) != ".":
           dirs.add(p.as_posix())
           p = p.parent


   dir_summaries: Dict[str, str] = {}


   # Deepest directories first.
   ordered_dirs = sorted(dirs, key=lambda d: d.count("/"), reverse=True)


   for d in ordered_dirs:
       pieces = []


       for rel, summary in file_summary_by_rel.items():
           if Path(rel).parent.as_posix() == d:
               pieces.append(f"### File: {rel}\n{summary}")


       for child_dir, summary in dir_summaries.items():
           if Path(child_dir).parent.as_posix() == d:
               pieces.append(f"### Subdirectory: {child_dir}\n{summary}")


       if not pieces:
           continue


       child_text = "\n\n".join(pieces)
       out_path = dir_out_base / f"{safe_filename(cluster_id)}__{safe_filename(d)}.md"
       log(f"  Summarizing directory node: {d}")
       dir_summaries[d] = summarize_directory(
           tokenizer,
           model,
           d,
           child_text,
           out_path,
           max_summary_chars,
           max_input_tokens,
           force,
       )


   return dir_summaries




# -----------------------------
# Main
# -----------------------------


def extract_title_description(text: str) -> Tuple[str, str]:
   title = ""
   description = text.strip()


   title_match = re.search(r"TITLE:\s*(.*)", text, flags=re.IGNORECASE)
   desc_match = re.search(r"DESCRIPTION:\s*(.*)", text, flags=re.IGNORECASE | re.DOTALL)


   if title_match:
       title = title_match.group(1).strip()


   if desc_match:
       description = desc_match.group(1).strip()


   description = re.sub(r"\s+", " ", description)


   words = description.split()
   if len(words) > 150:
       description = " ".join(words[:150])


   return title, description


def main() -> int:
   parser = argparse.ArgumentParser()
   parser.add_argument("--work-dir", default="/scratch/hpc-prf-dssecs/group4")
   parser.add_argument("--cluster-rsf", default="output/ARC_Qodo_alpha0_5_k10_clusters.rsf")
   parser.add_argument("--source-root", default=None)
   parser.add_argument("--output-dir", default="output/week4_hcag_arch_recovery")
   parser.add_argument("--model-name", default=os.environ.get("MODEL_NAME", "mistralai/Mixtral-8x7B-Instruct-v0.1"))
   parser.add_argument("--max-source-chars", type=int, default=int(os.environ.get("MAX_SOURCE_CHARS", "18000")))
   parser.add_argument("--max-summary-chars", type=int, default=int(os.environ.get("MAX_SUMMARY_CHARS", "28000")))
   parser.add_argument("--max-input-tokens", type=int, default=int(os.environ.get("MAX_INPUT_TOKENS", "4096")))
   parser.add_argument("--limit-clusters", type=int, default=0)
   parser.add_argument("--force", action="store_true")
   parser.add_argument("--no-4bit", action="store_true")
   args = parser.parse_args()


   work_dir = Path(args.work_dir).resolve()
   cluster_rsf = Path(args.cluster_rsf)
   if not cluster_rsf.is_absolute():
       cluster_rsf = work_dir / cluster_rsf


   out_dir = Path(args.output_dir)
   if not out_dir.is_absolute():
       out_dir = work_dir / out_dir


   leaf_dir = out_dir / "leaf_summaries"
   dir_dir = out_dir / "directory_summaries"
   cluster_dir = out_dir / "cluster_summaries"
   for d in [out_dir, leaf_dir, dir_dir, cluster_dir]:
       d.mkdir(parents=True, exist_ok=True)


   log("=" * 80)
   log("WEEK 4 HCAG HIERARCHICAL ARCHITECTURAL RECOVERY")
   log("=" * 80)
   log(f"Work dir: {work_dir}")
   log(f"Cluster RSF: {cluster_rsf}")
   log(f"Output dir: {out_dir}")
   log(f"Model: {args.model_name}")
   log(f"Generation temperature: {os.environ.get('GENERATION_TEMPERATURE', '0.0')}")
   log(f"Generation top_p: {os.environ.get('GENERATION_TOP_P', '0.9')}")
   log(f"CUDA available: {torch.cuda.is_available()}")
   if torch.cuda.is_available():
       log(f"GPU count: {torch.cuda.device_count()}")
       for i in range(torch.cuda.device_count()):
           log(f"GPU {i}: {torch.cuda.get_device_name(i)}")


   source_root = find_java_root(work_dir, args.source_root)
   log(f"Source root: {source_root}")


   clusters = parse_cluster_rsf(cluster_rsf)
   if args.limit_clusters and args.limit_clusters > 0:
       clusters = dict(list(clusters.items())[: args.limit_clusters])
       log(f"Limiting to first {args.limit_clusters} clusters for debug.")


   java_files, java_index = discover_java_files(source_root)
   log(f"Java files discovered: {len(java_files)}")
   log(f"Clusters discovered: {len(clusters)}")


   hf_token = os.environ.get("HF_TOKEN")
   if not hf_token:
       log("WARNING: HF_TOKEN is not set. Gated/private HF models may fail.")


   tokenizer, model = load_llm(args.model_name, hf_token, use_4bit=not args.no_4bit)


   cluster_rows = []
   unmatched_rows = []


   for c_idx, (cluster_id, entities) in enumerate(clusters.items(), start=1):
       log("\n" + "=" * 80)
       log(f"Processing cluster {c_idx}/{len(clusters)}: {cluster_id}")
       log(f"Entities in RSF cluster: {len(entities)}")


       matched: List[Tuple[str, Path]] = []
       seen_paths = set()


       for entity in entities:
           path = match_entity_to_file(entity, java_index)
           if path is None:
               unmatched_rows.append({"cluster_id": cluster_id, "entity": entity})
               continue
           if path not in seen_paths:
               matched.append((entity, path))
               seen_paths.add(path)


       log(f"Matched Java files: {len(matched)}")
       if not matched:
           log(f"WARNING: No matched Java files for cluster {cluster_id}; skipping.")
           continue


       file_summary_by_rel: Dict[str, str] = {}


       for f_idx, (entity, path) in enumerate(matched, start=1):
           rel = path.relative_to(source_root).as_posix()
           leaf_out = leaf_dir / safe_filename(cluster_id) / f"{safe_filename(rel)}.md"
           log(f"  Leaf {f_idx}/{len(matched)}: {rel}")
           summary = summarize_leaf(
               tokenizer,
               model,
               entity,
               path,
               source_root,
               leaf_out,
               args.max_source_chars,
               args.max_input_tokens,
               args.force,
           )
           file_summary_by_rel[rel] = summary


       dir_out_base = dir_dir / safe_filename(cluster_id)
       dir_out_base.mkdir(parents=True, exist_ok=True)
       dir_summaries = collect_directory_summaries(
           tokenizer,
           model,
           cluster_id,
           file_summary_by_rel,
           dir_out_base,
           args.max_summary_chars,
           args.max_input_tokens,
           args.force,
       )


       combined_pieces = []
       for rel, summary in file_summary_by_rel.items():
           combined_pieces.append(f"## File summary: {rel}\n{summary}")
       for d, summary in dir_summaries.items():
           combined_pieces.append(f"## Directory summary: {d}\n{summary}")


       combined_text = "\n\n".join(combined_pieces)
       cluster_out = cluster_dir / f"{safe_filename(cluster_id)}_architectural_summary.md"
       log(f"  Generating final cluster architectural summary: {cluster_id}")
       final_summary = summarize_cluster(
           tokenizer,
           model,
           cluster_id,
           combined_text,
           cluster_out,
           args.max_summary_chars,
           args.max_input_tokens,
           args.force,
       )


       title, description = extract_title_description(final_summary)
       cluster_rows.append(
           {
               "cluster_ID": cluster_id,
               "files": "; ".join(sorted(file_summary_by_rel.keys())),
               "title": title,
               "description": description,
           }
       )


       # Save progress after every cluster.
       pd_path = out_dir / "week4_cluster_architecture_summaries.csv"
       with pd_path.open("w", encoding="utf-8", newline="") as f:
           writer = csv.DictWriter(f, fieldnames=["cluster_ID", "files", "title", "description"])
           writer.writeheader()
           writer.writerows(cluster_rows)


   if unmatched_rows:
       unmatched_path = out_dir / "unmatched_entities.csv"
       with unmatched_path.open("w", encoding="utf-8", newline="") as f:
           writer = csv.DictWriter(f, fieldnames=["cluster_id", "entity"])
           writer.writeheader()
           writer.writerows(unmatched_rows)
       log(f"Unmatched entities saved: {unmatched_path}")


   report_path = out_dir / "week4_architectural_recovery_report.md"
   report_parts = [
       "# Week 4 LLM-Based Architectural Recovery Report\n",
       f"Model used: `{args.model_name}`\n",
       f"Cluster RSF: `{cluster_rsf}`\n",
       f"Source root: `{source_root}`\n",
       "\n## Cluster Summaries\n",
   ]


   for row in cluster_rows:
       summary_file = work_dir / row["summary_file"]
       report_parts.append(f"\n---\n\n## Cluster {row['cluster_id']}\n")
       report_parts.append(f"Matched Java files: {row['matched_java_files']}\n\n")
       report_parts.append(read_text(summary_file))
       report_parts.append("\n")


   write_text(report_path, "\n".join(report_parts))


   config = vars(args).copy()
   config.update(
       {
           "work_dir": str(work_dir),
           "cluster_rsf": str(cluster_rsf),
           "source_root": str(source_root),
           "output_dir": str(out_dir),
           "clusters_processed": len(cluster_rows),
           "unmatched_entities": len(unmatched_rows),
           "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
       }
   )
   write_text(out_dir / "week4_run_config.json", json.dumps(config, indent=2))


   log("\n" + "=" * 80)
   log("WEEK 4 JOB COMPLETED")
   log(f"Cluster summary CSV: {out_dir / 'week4_cluster_architecture_summaries.csv'}")
   log(f"Full report: {report_path}")
   log(f"Output directory: {out_dir}")
   log("=" * 80)
   return 0




if __name__ == "__main__":
   raise SystemExit(main())



