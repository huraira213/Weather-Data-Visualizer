from core.csv_reader import csvReader
from utils.file_utils import (get_csv_path, ensure_directory, get_full_path, list_csv_files)

class UserInterface:
    def __init__(self):
        self.csv_dir = get_csv_path()
        self.reader = csvReader(self.csv_dir)

    def run(self):
        print("-- Weather Data Visualizer --")
        print("1 Filter data")
        print("2. Load csv data")

    def load_csv(self):
        csv = self.reader.csv()
        if not csv:
            print("No csv file found.")
            print("-" * 30)
            return
        self.reader.list_csv_files()
        choice = input("Enter file number: ").strip()
        print("-" * 30)
        try:
            index = int(choice) - 1
            rows = self.reader.read_csv(logs[index])

        except (ValueError, IndexError):
            print("Invalid selection.")