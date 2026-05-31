#!/bin/bash

# =========================================================
# WEEK 4 HCAG ARCHITECTURAL RECOVERY - GROUP 4
# =========================================================

#SBATCH --job-name=group4_week4_hcag
#SBATCH --time=08:00:00
#SBATCH --gres=gpu:a100:2
#SBATCH --partition=gpu
#SBATCH --mem=240G
#SBATCH --cpus-per-task=16
#SBATCH --chdir=/scratch/hpc-prf-dssecs/group4
#SBATCH --output=logs/group4_week4_hcag_%j.log
#SBATCH --error=logs/group4_week4_hcag_%j.err

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
    "transformers==4.46.3" \
    "accelerate==1.0.1" \
    "bitsandbytes==0.44.1" \
    torch \
    transformers \
    accelerate \
    bitsandbytes \
    sentencepiece \
    protobuf \
    pandas \
    numpy \
    tqdm

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
# 6. MODEL + INPUT CONFIGURATION
# =========================================================

# Group 4 heavyweight option from the assignment that can realistically run locally.
# Change this to mistralai/Mistral-7B-Instruct-v0.3 for a faster debug run.
export MODEL_NAME="${MODEL_NAME:-mistralai/Mixtral-8x7B-Instruct-v0.1}"

# Keep source chunks bounded to avoid OOM.
export MAX_SOURCE_CHARS="${MAX_SOURCE_CHARS:-2000}"
export MAX_SUMMARY_CHARS="${MAX_SUMMARY_CHARS:-8000}"
export MAX_INPUT_TOKENS="${MAX_INPUT_TOKENS:-1024}"
# export OFFLOAD_DIR=/scratch/hpc-prf-dssecs/group4/cache/offload
# mkdir -p "$OFFLOAD_DIR"
# =========================================================
# 7. CHECKS
# =========================================================

echo "============================================================"
echo "GROUP 4 WEEK 4 HCAG ARCHITECTURAL RECOVERY JOB"
echo "============================================================"
echo "Job ID: ${SLURM_JOB_ID:-NO_JOB_ID}"
echo "Node: $HOSTNAME"
echo "Working directory: $(pwd)"
echo "Model: $MODEL_NAME"
echo "Start time: $(date)"
echo "============================================================"

echo "Checking GPU..."
nvidia-smi || true

echo "Checking required input files..."
ls -lah output/ARC_Qodo_alpha0_5_k10_clusters.rsf
ls -lah src || true
ls -lah week4_hcag_summary.py

python - <<'PYTEST'
import torch
print("CUDA available:", torch.cuda.is_available())
print("GPU count:", torch.cuda.device_count())
if torch.cuda.is_available():
    for i in range(torch.cuda.device_count()):
        print(f"GPU {i}:", torch.cuda.get_device_name(i))
PYTEST

# =========================================================
# 8. EXECUTION
# =========================================================

echo "Starting Week 4 HCAG hierarchical summarization..."

python week4_hcag_summary.py \
    --work-dir /scratch/hpc-prf-dssecs/group4 \
    --cluster-rsf output/ARC_Qodo_alpha0_5_k10_clusters.rsf \
    --output-dir output/week4_hcag_arch_recovery \
    --model-name "$MODEL_NAME" \
    --max-source-chars "$MAX_SOURCE_CHARS" \
    --max-summary-chars "$MAX_SUMMARY_CHARS" \
    --max-input-tokens "$MAX_INPUT_TOKENS"

echo "Week 4 job completed."
echo "Output folder:"
find output/week4_hcag_arch_recovery -maxdepth 3 -type f -printf "%p %s bytes\n" | head -200

echo "End time: $(date)"
echo "DONE"
