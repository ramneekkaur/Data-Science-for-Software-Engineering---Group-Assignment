#!/bin/bash

#SBATCH –job-name=week4_arc
#SBATCH –account=hpc-prf-dssecs
#SBATCH –partition=gpu
#SBATCH –qos=express_surabhi
#SBATCH –gres=gpu:a100:1
#SBATCH –time=04:00:00
#SBATCH –mem=80G
#SBATCH –cpus-per-task=8
#SBATCH –output=/scratch/hpc-prf-dssecs/surabhi/group4/week4_%j.out
#SBATCH –error=/scratch/hpc-prf-dssecs/surabhi/group4/week4_%j.err

set -euo pipefail

module purge
module load lang/Python/3.10.4-GCCcore-11.3.0
module load system/CUDA/12.4.0

cd /scratch/hpc-prf-dssecs/surabhi/group4

mkdir -p output/week4_results
mkdir -p cache/hf_cache

source ~/venv_/bin/activate

export HF_HOME=/scratch/hpc-prf-dssecs/surabhi/group4/cache/hf_cache
export HF_HUB_CACHE=/scratch/hpc-prf-dssecs/surabhi/group4/cache/hf_cache/hub
export TRANSFORMERS_CACHE=/scratch/hpc-prf-dssecs/surabhi/group4/cache/hf_cache/transformers

export TOKENIZERS_PARALLELISM=false

export MODEL_NAME=“google/flan-t5-base”

export MAX_SOURCE_CHARS=800
export MAX_SUMMARY_CHARS=2000
export MAX_INPUT_TOKENS=512

echo “==================================================”
echo “WEEK 4 HCAG RUN”
echo “==================================================”
echo “Node: $HOSTNAME”
echo “Start time: $(date)”
echo “Model: $MODEL_NAME”
echo “==================================================”

nvidia-smi || true

python week4_hcag_summary.py 
-work-dir /scratch/hpc-prf-dssecs/surabhi/group4 
-cluster-rsf output/ARC_Qodo_alpha0_5_k10_clusters.rsf 
-output-dir /scratch/hpc-prf-dssecs/surabhi/group4/output/week4_results 
-model-name “$MODEL_NAME” 
-max-source-chars “$MAX_SOURCE_CHARS” 
-max-summary-chars “$MAX_SUMMARY_CHARS” 
-max-input-tokens “$MAX_INPUT_TOKENS”

echo “==================================================”
echo “JOB FINISHED”
echo “==================================================”

find /scratch/hpc-prf-dssecs/surabhi/group4/output/week4_results -type f | head -50