#!/bin/bash

#SBATCH --job-name=week4_arc
#SBATCH --account=hpc-prf-dssecs
#SBATCH --partition=gpu
#SBATCH --qos=express_surabhi
#SBATCH --gres=gpu:a100:1
#SBATCH --time=04:00:00
#SBATCH --mem=80G
#SBATCH --cpus-per-task=8
#SBATCH --output=/scratch/hpc-prf-dssecs/surabhi/group4/week4_%j.out
#SBATCH --error=/scratch/hpc-prf-dssecs/surabhi/group4/week4_%j.err

set -euo pipefail

module purge
module load lang/Python/3.10.4-GCCcore-11.3.0
module load system/CUDA/12.4.0

cd /scratch/hpc-prf-dssecs/surabhi/group4

source ~/venv_/bin/activate

mkdir -p /scratch/hpc-prf-dssecs/surabhi/group4/cache/hf_cache
mkdir -p /scratch/hpc-prf-dssecs/surabhi/group4/output/week4_limbo_results

export HF_HOME=/scratch/hpc-prf-dssecs/surabhi/group4/cache/hf_cache
export HUGGINGFACE_HUB_CACHE=/scratch/hpc-prf-dssecs/surabhi/group4/cache/hf_cache
export TRANSFORMERS_CACHE=/scratch/hpc-prf-dssecs/surabhi/group4/cache/hf_cache
export HF_HUB_CACHE=/scratch/hpc-prf-dssecs/surabhi/group4/cache/hf_cache

export TOKENIZERS_PARALLELISM=false

export MODEL_NAME=microsoft/phi-2

echo Running with model: $MODEL_NAME

python week4_hcag_summary.py \
--work-dir /scratch/hpc-prf-dssecs/surabhi/group4 \
--cluster-rsf output/LIMBO_clusters_filelevel.rsf \
--source-root /scratch/hpc-prf-dssecs/surabhi/group4/src/lucene --output-dir /scratch/hpc-prf-dssecs/surabhi/group4/output/week4_limbo_results \
--model-name "$MODEL_NAME" \
--max-source-chars 500 \
--max-summary-chars 1000 \
--max-input-tokens 256