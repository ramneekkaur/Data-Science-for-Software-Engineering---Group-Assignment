#!/bin/bash

#SBATCH --job-name=group4_arc_week3
#SBATCH --time=04:00:00
#SBATCH --gres=gpu:a100:1
#SBATCH --partition=gpu
#SBATCH --mem=160G
#SBATCH --cpus-per-task=16
#SBATCH --chdir=/scratch/hpc-prf-dssecs/group4
#SBATCH --output=logs/group4_arc_week3_%j.log
#SBATCH --error=logs/group4_arc_week3_%j.err

set -euo pipefail

module purge
module load lang/Python/3.10.4-GCCcore-11.3.0
module load system/CUDA/12.4.0

cd /scratch/hpc-prf-dssecs/group4

mkdir -p logs output cache src arcade_eval
mkdir -p cache/hf_cache

if [ ! -d "/scratch/hpc-prf-dssecs/group4/venv_arc" ]; then
    echo "Creating virtual environment..."
    python -m venv /scratch/hpc-prf-dssecs/group4/venv_arc
fi

source /scratch/hpc-prf-dssecs/group4/venv_arc/bin/activate

echo "Installing/updating dependencies inside venv..."
python -m pip install --upgrade pip
python -m pip install \
    numpy \
    pandas \
    matplotlib \
    scikit-learn \
    scipy \
    torch \
    transformers \
    accelerate \
    sentence-transformers \
    huggingface_hub \
    jupyter \
    nbconvert \
    nbformat \
    nbclient \
    ipykernel

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

echo "============================================================"
echo "GROUP 4 WEEK 3 ARC NOTEBOOK JOB"
echo "Job ID: ${SLURM_JOB_ID:-NO_JOB_ID}"
echo "Node: $HOSTNAME"
echo "Working directory: $(pwd)"
echo "Notebook: dsseweek3arc.ipynb"
echo "Start time: $(date)"
echo "============================================================"

echo "Checking GPU..."
nvidia-smi || true

echo "Checking Python/CUDA..."
python - <<'PYTEST'
import torch
print("CUDA available:", torch.cuda.is_available())
print("GPU count:", torch.cuda.device_count())
if torch.cuda.is_available():
    print("GPU name:", torch.cuda.get_device_name(0))
PYTEST

echo "Checking input files..."
ls -lah input

echo "Checking notebook..."
ls -lah dsseweek3arc.ipynb

echo "============================================================"
echo "PATCHING NOTEBOOK"
echo "============================================================"

python - <<'PATCHNOTEBOOK'
import nbformat
from pathlib import Path

src = Path("dsseweek3arc.ipynb")
backup = Path("dsseweek3arc_BACKUP_BEFORE_SLURM_PATCH.ipynb")
patched = Path("dsseweek3arc_SLURM_PATCHED.ipynb")

if not src.exists():
    raise FileNotFoundError("dsseweek3arc.ipynb not found in /scratch/hpc-prf-dssecs/group4")

if not backup.exists():
    backup.write_bytes(src.read_bytes())
    print(f"Backup created: {backup}")

nb = nbformat.read(src, as_version=4)

changed = 0
skipped_install_cells = 0

for cell in nb.cells:
    if cell.get("cell_type") != "code":
        continue

    source = cell.get("source", "")
    old_source = source

    # Remove --user because Slurm runs inside venv_arc, and venv does not allow --user installs
    source = source.replace('"--user", ', "")
    source = source.replace("'--user', ", "")
    source = source.replace('"--user"', "")
    source = source.replace("'--user'", "")

    # Safer: if a cell only installs packages, turn it into a no-op because the .sh already installs packages
    if "pip" in source and "install" in source and "subprocess.check_call" in source:
        source = 'print("Skipping notebook pip install cell because dependencies are installed by Slurm job script.")'
        skipped_install_cells += 1

    if source != old_source:
        cell["source"] = source
        changed += 1

nbformat.write(nb, patched)

print(f"Patched notebook saved as: {patched}")
print(f"Cells changed: {changed}")
print(f"Pip install cells skipped: {skipped_install_cells}")

# hard check
text = patched.read_text(encoding="utf-8")
if "--user" in text:
    print("WARNING: --user still appears somewhere in the patched notebook text.")
else:
    print("OK: patched notebook contains no --user.")
PATCHNOTEBOOK

echo "============================================================"
echo "CREATING PROGRESS RUNNER"
echo "============================================================"

cat > run_notebook_with_progress.py <<'PYRUNNER'
from pathlib import Path
import traceback
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

notebook_path = Path("dsseweek3arc_SLURM_PATCHED.ipynb")
output_path = Path("dsseweek3arc_EXECUTED.ipynb")

print(f"Loading notebook: {notebook_path}", flush=True)

with notebook_path.open("r", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

total_cells = len(nb.cells)
print(f"Total cells: {total_cells}", flush=True)

class ProgressExecutePreprocessor(ExecutePreprocessor):
    def preprocess_cell(self, cell, resources, index):
        cell_type = cell.get("cell_type", "unknown")
        source = str(cell.get("source", "")).strip()
        first_line = source.splitlines()[0][:180] if source else ""

        print("\n" + "=" * 100, flush=True)
        print(f"STARTING CELL {index + 1}/{total_cells} | type={cell_type}", flush=True)
        if first_line:
            print(f"First line: {first_line}", flush=True)
        print("=" * 100, flush=True)

        try:
            result = super().preprocess_cell(cell, resources, index)
            print(f"FINISHED CELL {index + 1}/{total_cells}", flush=True)
            return result
        except Exception as e:
            print("\n" + "!" * 100, flush=True)
            print(f"FAILED AT CELL {index + 1}/{total_cells}", flush=True)
            if first_line:
                print(f"First line: {first_line}", flush=True)
            print("Error type:", type(e).__name__, flush=True)
            print("Error message:", str(e), flush=True)
            print("Traceback:", flush=True)
            traceback.print_exc()
            print("!" * 100 + "\n", flush=True)

            with output_path.open("w", encoding="utf-8") as f:
                nbformat.write(nb, f)
            print(f"Partial executed notebook saved to: {output_path}", flush=True)

            raise

ep = ProgressExecutePreprocessor(
    timeout=-1,
    kernel_name="python3",
    allow_errors=False,
)

resources = {
    "metadata": {
        "path": str(Path.cwd())
    }
}

print("Starting notebook execution...", flush=True)

ep.preprocess(nb, resources)

print(f"Writing executed notebook: {output_path}", flush=True)

with output_path.open("w", encoding="utf-8") as f:
    nbformat.write(nb, f)

print("Notebook execution completed successfully.", flush=True)
PYRUNNER

echo "============================================================"
echo "EXECUTING NOTEBOOK WITH CELL-BY-CELL PROGRESS"
echo "============================================================"

python run_notebook_with_progress.py

echo "============================================================"
echo "NOTEBOOK EXECUTION FINISHED"
echo "============================================================"

echo "Output folder:"
ls -lah output || true

echo "Arcade evaluation folder:"
find arcade_eval -maxdepth 3 -type f -printf "%p %s bytes\n" 2>/dev/null || true

echo "End time: $(date)"
echo "DONE"