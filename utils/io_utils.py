# utils/io_utils.py
import csv
import random
from datetime import datetime, timedelta
from pathlib import Path
from utils.paths import INPUT_DIR, ensure_directory


def list_csv_files(folder: Path) -> list[str]:
    """Return a list of all CSV file names in the folder."""
    ensure_directory(folder)
    return [f.name for f in folder.glob("*.csv")]


def create_sample_csv():
    """Create a random weather CSV file for testing."""
    ensure_directory(INPUT_DIR)
    sample_path = INPUT_DIR / "sample2.csv"

    with open(sample_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["date", "temperature", "humidity", "rainfall", "condition"])

        start_date = datetime(2025, 10, 1)
        conditions = ["Sunny", "Cloudy", "Rainy", "Stormy", "Hot"]

        for i in range(22):
            date = (start_date + timedelta(days=i)).strftime("%Y-%m-%d")
            temp = round(random.uniform(25, 35), 1)
            humidity = random.randint(35, 70)
            rainfall = round(random.uniform(0, 15), 1)
            condition = random.choice(conditions)
            writer.writerow([date, temp, humidity, rainfall, condition])

    print(f"Sample CSV created at {sample_path}")
