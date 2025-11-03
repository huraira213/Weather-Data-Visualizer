import csv
from pathlib import Path
from utils.paths import (get_csv_path, ensure_directory)
from utils.io_utils import list_csv_files

class CsvReader:
    """Handles reading and listing CSV files"""
    def __init__(self, csv_dir: str):
        self.csv_dir = Path(csv_dir)
        ensure_directory(self.csv_dir)

    def list_csv_files(self):
        """Lists all CSV files in the csv_dir"""
        csv_files = list_csv_files(self.csv_dir)
        if not csv_files:
            print("No CSV files found")
        return csv_files

    def read_csv(self, csv_file):
        """Reads a CSV file"""
        try:
            csv_path = get_csv_path() / csv_file

            if not csv_path.exists():
                raise FileNotFoundError(f"File {csv_path} does not exist")

            with open(csv_path, newline='') as file:
                reader =csv.DictReader(file)
                return [row for row in reader]


        except FileNotFoundError:
            print(f"{csv_file} not found. Returning empty list.")
            return []
        except Exception as e:
            print(f"Error reading from {csv_file}: {e}")
            return []
