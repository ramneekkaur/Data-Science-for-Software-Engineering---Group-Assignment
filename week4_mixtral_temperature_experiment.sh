#!/bin/bash

# =========================================================
# WEEK 4 MIXTRAL TEMPERATURE EXPERIMENT - GROUP 4
# Runs HCAG architectural recovery with Mixtral at multiple temperatures.
# Results are saved in separate output folders for each temperature.
# =========================================================

#SBATCH --job-name=group4_w4_mixtral_temp
#SBATCH --time=12:00:00
#SBATCH --gres=gpu:a100:2
#SBATCH --partition=gpu
#SBATCH --mem=240G
#SBATCH --cpus-per-task=16
#SBATCH --chdir=/scratch/hpc-prf-dssecs/group4
#SBATCH --output=logs/group4_w4_mixtral_temp_%j.log
#SBATCH --error=logs/group4_w4_mixtral_temp_%j.err

set -euo pipefail

# =========================================================
# 1. LOAD MODULES
# =========================================================

module purge
module load lang/Python/3.10.4-GCCcore-11.3.0
module load system/CUDA/12.4.0

# =========================================================
# 2. PROJECT SETUP
# =========================================================

cd /scratch/hpc-prf-dssecs/group4
mkdir -p logs output cache src arcade_eval
mkdir -p cache/hf_cache

# =========================================================
# 3. VIRTUAL ENVIRONMENT
# =========================================================

if [ ! -d "/scratch/hpc-prf-dssecs/group4/venv_week4" ]; then
    echo "Creating Week 4 virtual environment..."
    python -m venv /scratch/hpc-prf-dssecs/group4/venv_week4
fi

source /scratch/hpc-prf-dssecs/group4/venv_week4/bin/activate

# =========================================================
# 4. DEPENDENCIES
# =========================================================

echo "Installing/updating Week 4 dependencies..."
python -m pip install --upgrade pip
python -m pip install \
    torch \
    transformers \
    accelerate \
    bitsandbytes \
    sentencepiece \
    protobuf \
    pandas \
    numpy \
    tqdm \
    nbformat

# =========================================================
# 5. HUGGING FACE CACHE + TOKEN
# =========================================================

export HF_HOME=/scratch/hpc-prf-dssecs/group4/cache/hf_cache
export HF_HUB_CACHE=/scratch/hpc-prf-dssecs/group4/cache/hf_cache/hub
export TRANSFORMERS_CACHE=/scratch/hpc-prf-dssecs/group4/cache/hf_cache/transformers
export TOKENIZERS_PARALLELISM=false
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True,max_split_size_mb:512

TOKEN_FILE="/scratch/hpc-prf-dssecs/rohit/hf_cache/token"

if [ -f "$TOKEN_FILE" ]; then
    export HF_TOKEN=$(cat "$TOKEN_FILE" | tr -d '[:space:]')
    echo "HF_TOKEN loaded from token file."
else
    echo "ERROR: Hugging Face token file not found at $TOKEN_FILE"
    exit 1
fi

# =========================================================
# 6. EXPERIMENT CONFIGURATION
# =========================================================

export MODEL_NAME="mistralai/Mixtral-8x7B-Instruct-v0.1"
export GENERATION_TOP_P="0.90"

# Keep context bounded to avoid OOM. Increase only if stable.
export MAX_SOURCE_CHARS="${MAX_SOURCE_CHARS:-14000}"
export MAX_SUMMARY_CHARS="${MAX_SUMMARY_CHARS:-22000}"
export MAX_INPUT_TOKENS="${MAX_INPUT_TOKENS:-3072}"

# Optional debug mode: submit with
# sbatch --export=ALL,LIMIT_CLUSTERS=1 week4_mixtral_temperature_experiment.sh
export LIMIT_CLUSTERS="${LIMIT_CLUSTERS:-0}"

TEMPERATURES=("0.1" "0.3" "0.7")

# =========================================================
# 7. BASIC CHECKS
# =========================================================

echo "============================================================"
echo "GROUP 4 WEEK 4 MIXTRAL TEMPERATURE EXPERIMENT"
echo "============================================================"
echo "Job ID: ${SLURM_JOB_ID:-NO_JOB_ID}"
echo "Node: $HOSTNAME"
echo "Working directory: $(pwd)"
echo "Model: $MODEL_NAME"
echo "Temperatures: ${TEMPERATURES[*]}"
echo "MAX_SOURCE_CHARS: $MAX_SOURCE_CHARS"
echo "MAX_SUMMARY_CHARS: $MAX_SUMMARY_CHARS"
echo "MAX_INPUT_TOKENS: $MAX_INPUT_TOKENS"
echo "LIMIT_CLUSTERS: $LIMIT_CLUSTERS"
echo "Start time: $(date)"
echo "============================================================"

echo "Checking GPU..."
nvidia-smi || true

echo "Checking required files..."
ls -lah week4_hcag_summary.py
ls -lah output/ARC_Qodo_alpha0_5_k10_clusters.rsf
ls -lah src || true

python - <<'PYTEST'
import torch
print("CUDA available:", torch.cuda.is_available())
print("GPU count:", torch.cuda.device_count())
if torch.cuda.is_available():
    for i in range(torch.cuda.device_count()):
        print(f"GPU {i}:", torch.cuda.get_device_name(i))
PYTEST

# =========================================================
# 8. PATCH week4_hcag_summary.py TO SUPPORT TEMPERATURE
# =========================================================

echo "Patching week4_hcag_summary.py for temperature experiment..."

python - <<'PYPATCH'
from pathlib import Path
import py_compile

path = Path("week4_hcag_summary.py")
backup = Path("week4_hcag_summary_BACKUP_BEFORE_TEMP_EXPERIMENT.py")

if not path.exists():
    raise FileNotFoundError("week4_hcag_summary.py not found in /scratch/hpc-prf-dssecs/group4")

text = path.read_text(encoding="utf-8")

if not backup.exists():
    backup.write_text(text, encoding="utf-8")
    print(f"Backup created: {backup}")

# Fix accidental duplicated line if present from earlier edits.
text = text.replace("summary = generate_text(\n    summary = generate_text(", "summary = generate_text(")

old_block = '''    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=False,
            temperature=None,
            top_p=None,
            pad_token_id=tokenizer.eos_token_id,
            eos_token_id=tokenizer.eos_token_id,
            use_cache=False,
        )
'''

new_block = '''    generation_temperature = float(os.environ.get("GENERATION_TEMPERATURE", "0.0"))
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
'''

if old_block in text:
    text = text.replace(old_block, new_block)
    print("Generation block patched for temperature support.")
elif "generation_temperature = float(os.environ.get" in text:
    print("Temperature support already present.")
else:
    raise RuntimeError("Could not find the generation block to patch. Please inspect week4_hcag_summary.py around model.generate().")

old_log = '    log(f"Model: {args.model_name}")\n'
new_log = '    log(f"Model: {args.model_name}")\n    log(f"Generation temperature: {os.environ.get(\'GENERATION_TEMPERATURE\', \'0.0\')}")\n    log(f"Generation top_p: {os.environ.get(\'GENERATION_TOP_P\', \'0.9\')}")\n'
if old_log in text and "Generation temperature" not in text:
    text = text.replace(old_log, new_log)

path.write_text(text, encoding="utf-8")
py_compile.compile(str(path), doraise=True)
print("week4_hcag_summary.py syntax check passed.")
PYPATCH

# =========================================================
# 9. RUN TEMPERATURE EXPERIMENTS
# =========================================================

EXPERIMENT_ROOT="output/week4_mixtral_temperature_experiment"
mkdir -p "$EXPERIMENT_ROOT"

INDEX_FILE="$EXPERIMENT_ROOT/temperature_experiment_index.csv"
echo "temperature,output_dir,status,start_time,end_time" > "$INDEX_FILE"

for TEMP in "${TEMPERATURES[@]}"; do
    TEMP_LABEL=$(echo "$TEMP" | sed 's/\./p/g')
    OUT_DIR="$EXPERIMENT_ROOT/temp_${TEMP_LABEL}"
    mkdir -p "$OUT_DIR"

    export GENERATION_TEMPERATURE="$TEMP"

    START_TIME=$(date '+%Y-%m-%d %H:%M:%S')

    echo "============================================================"
    echo "STARTING TEMPERATURE RUN: $TEMP"
    echo "Output dir: $OUT_DIR"
    echo "Start time: $START_TIME"
    echo "============================================================"

    LIMIT_ARGS=()
    if [ "$LIMIT_CLUSTERS" != "0" ]; then
        LIMIT_ARGS=(--limit-clusters "$LIMIT_CLUSTERS")
    fi

    set +e
    python week4_hcag_summary.py \
        --work-dir /scratch/hpc-prf-dssecs/group4 \
        --cluster-rsf output/ARC_Qodo_alpha0_5_k10_clusters.rsf \
        --output-dir "$OUT_DIR" \
        --model-name "$MODEL_NAME" \
        --max-source-chars "$MAX_SOURCE_CHARS" \
        --max-summary-chars "$MAX_SUMMARY_CHARS" \
        --max-input-tokens "$MAX_INPUT_TOKENS" \
        --force \
        "${LIMIT_ARGS[@]}"
    STATUS_CODE=$?
    set -e

    END_TIME=$(date '+%Y-%m-%d %H:%M:%S')

    if [ "$STATUS_CODE" -eq 0 ]; then
        STATUS="completed"
        echo "TEMPERATURE RUN $TEMP COMPLETED"
    else
        STATUS="failed_exit_${STATUS_CODE}"
        echo "TEMPERATURE RUN $TEMP FAILED with exit code $STATUS_CODE"
    fi

    echo "$TEMP,$OUT_DIR,$STATUS,$START_TIME,$END_TIME" >> "$INDEX_FILE"

    echo "Current files for $TEMP:"
    find "$OUT_DIR" -maxdepth 2 -type f -printf "%p %s bytes\n" | head -100 || true

    if [ "$STATUS_CODE" -ne 0 ]; then
        echo "Stopping experiment because temperature $TEMP failed."
        exit "$STATUS_CODE"
    fi

done

# =========================================================
# 10. FINAL SUMMARY
# =========================================================

echo "============================================================"
echo "MIXTRAL TEMPERATURE EXPERIMENT FINISHED"
echo "Index file: $INDEX_FILE"
echo "Generated outputs:"
find "$EXPERIMENT_ROOT" -maxdepth 3 -type f -printf "%p %s bytes\n" | head -300
cat "$INDEX_FILE"
echo "End time: $(date)"
echo "DONE"
echo "============================================================"
