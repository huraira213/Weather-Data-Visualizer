# utils/paths.py
from pathlib import Path

# === Base directories ===
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
INPUT_DIR = DATA_DIR / "input"
OUTPUT_DIR = DATA_DIR / "output"

# === Path functions ===
def ensure_directory(path: Path) -> None:
    """Ensure a directory exists; create if missing."""
    path.mkdir(parents=True, exist_ok=True)

def get_csv_path() -> Path:
    """Return absolute path to the input CSV folder."""
    ensure_directory(INPUT_DIR)
    return INPUT_DIR

def get_output_path(filename: str) -> Path:
    """Return absolute output path for a given filename."""
    ensure_directory(OUTPUT_DIR)
    return OUTPUT_DIR / filename
