# Data Science for Software Engineering-Group Assignment
Here's the complete README as plain text that you can copy and paste:

```
# Data Science for Software Engineering - Group Assignment

A comprehensive software architecture recovery pipeline for the Lucene Codecs project, combining **comparison-based clustering (Week 3)** with **hierarchical architectural discovery (Week 4)** using advanced NLP and machine learning techniques.

## Project Overview

This project performs two-stage architectural analysis on Java source code:

1. **Stage 1 (Week 3): Architectural Comparisons via ARC Clustering**
   - Uses semantic embeddings and structural analysis to partition code into architectural clusters
   - Compares multiple baseline clustering methods (WCA_UEM, WCA_UEMNM, LIMBO_IL)
   - Produces cluster assignments with combined semantic + structural similarity metrics

2. **Stage 2 (Week 4): Hierarchical Architectural Discovery**
   - Performs bottom-up summarization from raw Java files to architectural clusters
   - Uses Large Language Models (Mixtral or other LLMs) for intelligent code understanding
   - Generates human-readable architectural descriptions and cluster summaries

## Repository Structure

```
├── DS4SE26_Week3_ARC_PC2.ipynb          # Week 3 main notebook - ARC clustering
├── week4_hcag_summary.py                # Week 4 main script - HCAG architectural recovery
├── output/                              # Generated outputs
│   ├── ARC_Qodo_alpha0_5_k10_*.rsf     # Cluster definitions (ARCADE RSF format)
│   ├── ARC_Qodo_alpha0_5_k10_*.csv     # Cluster assignments in CSV
│   ├── ARC_Qodo_alpha0_5_k10_*_matrix.npy  # Similarity/distance matrices
│   ├── week4_hcag_arch_recovery/       # Week 4 architectural outputs
│   │   ├── leaf_summaries/             # File-level summaries
│   │   ├── directory_summaries/        # Module-level summaries
│   │   ├── cluster_summaries/          # Final cluster architectural descriptions
│   │   └── week4_cluster_architecture_summaries.csv
│   └── week4_architectural_recovery_report.md
├── class_dependency_extraction/         # Dependency extraction utilities
├── input/                              # Input data (baseline RSFs, Java source)
├── cache/                              # Hugging Face model cache
├── run_week4_arc.sh                    # Script to run Week 3 via SLURM
├── run_week4_limbo.sh                  # Script to run Week 4 via SLURM
└── week4_hcag_summary.py               # Architectural recovery pipeline
```

## Technologies & Tools

**Language Composition:**
- Jupyter Notebook: 81.3%
- Python: 13.9%
- Shell: 4.8%

**Key Libraries:**
- **Transformers & Embeddings**: `sentence-transformers`, `transformers` (Mixtral-8x7B for LLM-based summarization)
- **Data Science**: `numpy`, `pandas`, `scikit-learn`, `scipy`
- **Deep Learning**: `torch`, `cuda-toolkit`
- **Code Analysis**: Custom RSF parsing and Java dependency extraction

---

## Stage 1: Week 3 - Architectural Comparisons (ARC Clustering)

### Purpose
Compare semantic and structural similarities in Java code to identify coherent architectural clusters. The process combines:
- **Semantic similarity**: Code embeddings from Qodo/Qodo-Embed-1-7B
- **Structural similarity**: Dependency graph analysis (RSF format)
- **Weighted combination**: Parameterized blending (α = 0.5)

### Input Data

Required input files in `input/` directory:
- `lucene-codecs-focused.rsf` - Focused dependency relationships (Week 1)
- `wca_uem.rsf` - WCA_UEM baseline clustering
- `wca_uemnm.rsf` - WCA_UEMNM baseline clustering
- `limbo_il.rsf` - LIMBO_IL baseline clustering

### Key Configuration (Week 3)

```python
EMBEDDING_MODEL_NAME = "Qodo/Qodo-Embed-1-7B"
ALPHA = 0.50                    # Semantic vs. structural weight balance
TARGET_NUM_CLUSTERS = 10        # Desired number of clusters
BATCH_SIZE = 1                  # Processing batch size
MAX_TOKENS = 1024               # Token limit per chunk
LUCENE_GIT_TAG = "releases/lucene/9.10.0"
```

### Process Flow

1. **Load Data**: Parse RSF files, discover Java source files
2. **Generate Embeddings**: Use Qodo embeddings for all entities
3. **Build Similarity Matrices**:
   - Semantic: Entity embeddings → cosine similarity
   - Structural: RSF dependency graph → adjacency-based similarity
4. **Combine Matrices**: `combined = α × semantic + (1-α) × structural`
5. **Perform Clustering**: Hierarchical clustering on combined similarity
6. **Output Artifacts**:
   - `ARC_Qodo_alpha0_5_k10_clusters.rsf` - Standard ARCADE format
   - `ARC_Qodo_alpha0_5_k10_clusters.csv` - Human-readable assignments
   - `*_matrix.npy` files - Intermediate matrices for analysis
   - Comparison CSV with baseline metrics

### How to Run Week 3

**Interactive Mode (Notebook):**
```bash
jupyter notebook DS4SE26_Week3_ARC_PC2.ipynb
```

**Batch Mode (SLURM on HPC):**
```bash
sbatch run_week4_arc.sh
```

### Week 3 Output Summary

From `ARC_Qodo_alpha0_5_k10_summary.txt`:
- **Java source files**: 93 files analyzed
- **RSF edges**: 1947 dependency relationships
- **Unique entities**: 343 identified
- **Overlapping entities**: 53 (source ↔ RSF mapping)
- **Clusters**: 10 architectural clusters produced
- **Outputs**: RSF, CSV, matrices, visualization PNG

---

## Stage 2: Week 4 - Hierarchical Architectural Discovery

### Purpose
Perform **bottom-up hierarchical code summarization** using LLMs to produce human-readable architectural descriptions. The process:
1. Summarizes individual Java files (leaf nodes)
2. Aggregates file summaries into directory/module descriptions
3. Synthesizes directory summaries into final cluster architectural narratives

### How It Works

#### Leaf Summarization (File Level)
- **Input**: Raw Java source code
- **Processing**: LLM analyzes each file with structured prompts
- **Output**: Semantic file summary with:
  - File title and key functionality
  - Core logic and control flow
  - Input/output interfaces
  - Dependencies (internal & external)
  - Architectural role
  - Important classes/methods

#### Directory Summarization (Module Level)
- **Input**: Child summaries only (NO raw code)
- **Processing**: LLM synthesizes summaries in bottom-up order
- **Output**: Module-level description with:
  - Directory/module title
  - High-level responsibilities
  - How child components interact
  - Architectural role within cluster

#### Cluster Summarization (Final Level)
- **Input**: All file + directory summaries
- **Processing**: LLM generates final architectural narrative
- **Output**: Cluster architectural description with:
  - Architectural title
  - High-level summary (≤150 words)
  - Main responsibilities
  - Key components and interactions
  - External dependencies
  - Cohesion justification

### Input Data

- **Cluster RSF**: `output/ARC_Qodo_alpha0_5_k10_clusters.rsf` (from Week 3)
- **Java Source Root**: Auto-detected or specified via `--source-root`
- **Model**: Mixtral-8x7B or custom LLM (via `--model-name`)

### Key Configuration (Week 4)

```python
# Model selection
MODEL_NAME = "mistralai/Mixtral-8x7B-Instruct-v0.1"

# Text processing
MAX_SOURCE_CHARS = 18000           # Max chars per Java file
MAX_SUMMARY_CHARS = 28000          # Max chars per summary batch
MAX_INPUT_TOKENS = 4096            # Tokenizer input limit

# Generation
GENERATION_TEMPERATURE = 0.0       # Deterministic output (0.0)
GENERATION_TOP_P = 0.9             # Nucleus sampling (if temp > 0)
```

### Process Flow

1. **Discover Java Files**: Recursively find `.java` files, skip build artifacts
2. **Entity Matching**: Map RSF entities → Java file paths (handles package naming variations)
3. **Hierarchical Summarization**:
   - For each cluster:
     - Summarize each matched Java file (parallel capable)
     - Build directory tree from file paths
     - Bottom-up: summarize deepest dirs → root
     - Final: cluster-level synthesis
4. **Output Generation**:
   - `leaf_summaries/` - Individual file summaries (Markdown)
   - `directory_summaries/` - Module summaries (Markdown)
   - `cluster_summaries/` - Final architectural descriptions (Markdown)
   - `week4_cluster_architecture_summaries.csv` - Summary table
   - `week4_architectural_recovery_report.md` - Full report
   - `unmatched_entities.csv` - Entities without Java files

### How to Run Week 4

**Interactive Python:**
```bash
python week4_hcag_summary.py \
  --work-dir /scratch/hpc-prf-dssecs/group4 \
  --cluster-rsf output/ARC_Qodo_alpha0_5_k10_clusters.rsf \
  --output-dir output/week4_hcag_arch_recovery \
  --model-name mistralai/Mixtral-8x7B-Instruct-v0.1
```

**Batch Mode (SLURM with 2 A100 GPUs):**
```bash
sbatch run_week4_limbo.sh
```

**With Custom Temperature (more creative output):**
```bash
export GENERATION_TEMPERATURE=0.3
export GENERATION_TOP_P=0.95
python week4_hcag_summary.py --force
```

### Week 4 Output Files

**Primary Outputs:**
- `week4_cluster_architecture_summaries.csv` - Table of cluster IDs, files, titles, descriptions
- `week4_architectural_recovery_report.md` - Full markdown report with all summaries
- `week4_run_config.json` - Configuration and run metadata

**Intermediate Outputs:**
- `leaf_summaries/` - Per-file summaries in `cluster_id/file.md`
- `directory_summaries/` - Per-directory summaries
- `cluster_summaries/` - Final `cluster_id_architectural_summary.md`

**Diagnostic Outputs:**
- `unmatched_entities.csv` - RSF entities without corresponding Java files

---

## Data Formats

### RSF Format (ARCADE)
```
# ARCADE RSF format for clusters
contain Cluster1 Entity1
contain Cluster1 Entity2
contain Cluster2 Entity3
...
```

### CSV Format (Week 3 Clusters)
```csv
cluster_ID,entity,file
Cluster1,org.apache.lucene.codecs.Codec,org/apache/lucene/codecs/Codec.java
...
```

### CSV Format (Week 4 Architecture Summaries)
```csv
cluster_ID,files,title,description
Cluster1,"file1.java; file2.java",Codec Interface Module,"Defines the core API..."
...
```

---

## Key Findings

Based on Week 3 ARC clustering with α=0.5:
- **10 architectural clusters** identified from 93 Java files
- **Semantic + Structural blending** improves over single-method baselines
- **Comparison results** saved in `ARC_Qodo_alpha0_5_k10_python_comparison_sanity.csv`
- **Baseline comparison**: WCA_UEM, WCA_UEMNM, LIMBO_IL methods evaluated

Based on Week 4 architectural recovery:
- **Hierarchical summarization** produces coherent architectural narratives
- **LLM-based analysis** captures semantic intent and responsibilities
- **Bottom-up synthesis** ensures consistency across hierarchy levels
- **Output**: Human-readable cluster descriptions suitable for documentation

---

## Dependencies & Requirements

### Python Packages
- `torch` (≥2.0) with CUDA support
- `transformers` (≥5.0)
- `sentence-transformers` (≥5.0)
- `numpy`, `pandas`, `scikit-learn`, `scipy`
- `huggingface_hub`

### Hardware
- **Week 3**: 1-2 GPUs (or CPU with longer runtime)
- **Week 4**: 2× A100 GPUs (Mixtral) or 1× GPU (smaller models)

### Environment Variables
```bash
export HF_HOME=/path/to/hf_cache
export HF_TOKEN=your_hf_token       # For gated models
export GENERATION_TEMPERATURE=0.0   # Week 4 LLM temperature
export GENERATION_TOP_P=0.9         # Week 4 nucleus sampling
```

---

## Troubleshooting

### Week 3 Issues

**ModuleNotFoundError (pandas, torch, etc.)**
- Restart Jupyter kernel
- Rerun Cell 1 (PATH setup) and Cell 2 (package installation)
- Check `~/.local/lib/python3.10/site-packages/`

**GPU/CUDA not detected**
- Verify CUDA version: `nvidia-smi`
- Check driver: `python -c "import torch; print(torch.cuda.is_available())"`

### Week 4 Issues

**Entity matching failures (unmatched_entities.csv)**
- Verify Java source root location
- Check package name consistency in RSF vs. source
- Use `--source-root` flag if auto-detection fails

**LLM memory errors**
- Reduce `--max-source-chars` or `--max-input-tokens`
- Use a smaller model: `--model-name mistralai/Mistral-7B-Instruct-v0.1`
- Enable 4-bit quantization (default)

**Generation too slow**
- Check GPU availability: `torch.cuda.device_count()`
- Use quantization: `--no-4bit` to disable (try if buggy)
- Reduce `--limit-clusters` for testing

---

## References & Attribution

**Week 3 (ARC Clustering):**
- Based on ARCADE tool suite
- Qodo embeddings: https://huggingface.co/Qodo/Qodo-Embed-1-7B

**Week 4 (Hierarchical Recovery):**
- Inspired by HCAG (Hierarchical Code Architecture Generation)
- LLM-based architecture recovery techniques
- Supported models: Mixtral-8x7B, Mistral-7B, others

**Baseline Comparisons:**
- WCA_UEM (Weighted Context-Aware clustering)
- LIMBO_IL (Latent Semantic Indexing + hierarchical clustering)

---

## License & Citation

This is a group assignment for the Data Science for Software Engineering course.

**Authors**: Group 4
**Course**: Data Science for Software Engineering (DS4SE 2026)
**Assignment 1**: Weeks 3-4 (Architectural Comparisons & Hierarchical Discovery)

---

## Questions & Support

For issues or questions:
1. Check the troubleshooting section above
2. Review output logs in `logs/` and `output/`
3. Consult `.sh` script logs from SLURM runs
4. Check Jupyter cell outputs and error messages

---
