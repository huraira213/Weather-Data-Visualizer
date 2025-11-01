#file_utils.py
import random
from datetime import datetime, timedelta
from pathlib import Path

def get_csv_path() -> Path:
    return Path("data/input").resolve()

def ensure_directory(path: Path) -> None:
    """Ensure the directory exists. Create if missing."""
    path.mkdir(parents=True, exist_ok=True)

def get_full_path(*parts: str) -> Path:
    """Safely join paths and return a Path object."""
    return Path(*parts).resolve()

def list_csv_files(log_folder: Path) -> list[str]:
    """Return a list of all .log file names in the given folder."""
    return [f.name for f in log_folder.glob("*.csv")]



def create_sample_csv():
    with open('data/input/sample.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['date', 'temperature', 'humidity', 'rainfall', 'condition'])

        start_date = datetime(2025, 10, 1)
        conditions = ['Sunny', 'Cloudy', 'Rainy', 'Stormy', 'Hot']

        for i in range(12):
            date = (start_date + timedelta(days=i)).strftime('%Y-%m-%d')
            temp = round(random.uniform(25, 35), 1)
            humidity = random.randint(35, 70)
            rainfall = round(random.uniform(0, 15), 1)
            condition = random.choice(conditions)
            writer.writerow([date, temp, humidity, rainfall, condition])
