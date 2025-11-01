import os
from pathlib import Path
from utils.file_utils import (get_csv_path, ensure_directory, get_full_path, list_csv_files)

class csvReader:
    """Handles reading and listing CSV files"""
    def __init__(self, csv_dir:str):
        self.csv_dir = path(csv_dir)
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
            path = get_full_path(self.csv_dir, csv_file)

            if not path.exists():
                raise FileNotFoundError(f"File {path} does not exist")

            with open(path, newline='') as file:

        except FileNotFoundError:
            print(f"{file_name} not found. Returning empty list.")
            return []
        except Exception as e:
            print(f"Error reading from {file_name}: {e}")
            return []
