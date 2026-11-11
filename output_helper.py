import json
import subprocess
import sys
from pathlib import Path

folder = Path(__file__).resolve().parent
command = [sys.executable, "reference.py"]

result = subprocess.run(
    command,
    cwd=folder,
    capture_output=True,
    text=True,
)

record = {
    "command": "py reference.py",
    "returncode": result.returncode,
    "stdout": result.stdout,
    "stderr": result.stderr,
}

output_file = folder / "verification.json"
output_file.write_text(
    json.dumps(record, indent=2),
    encoding="utf-8",
)

print(f"Saved output to {output_file.name}")
print(f"Exit code: {result.returncode}")