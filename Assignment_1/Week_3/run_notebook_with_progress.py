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
