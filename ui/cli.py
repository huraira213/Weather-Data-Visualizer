#ui/cli.py
from core.reader import CsvReader
from core.analyzer import CsvAnalyzer
from core.report import ReportGenerator
from core.processor import process_data
from core.visualizer import DataVisualizer
from utils.paths import (get_csv_path)



class UserInterface:
    def __init__(self):
        self.csv_dir = get_csv_path()
        self.reader = CsvReader(self.csv_dir)
        self.analyzer = CsvAnalyzer()




    def display_menu(self):
        print("-- Weather Data Visualizer --")
        print("=" * 30)
        print("1. Read CSV")
        print("2. Analyze data")
        print("3. Generate report")
        print("4. Visualize data")  # new
        print("5. Exit")
        print("-" * 30)

    def analyzer_menu(self):
        print("-- Some data operations --")
        print("=" * 30)
        print("1. Get summary")
        print("2. Get hottest day")
        print("3. Get coldest day")
        print("4. Get total rainfall")
        print("5. Get average temperature")
        print("6. Get average humidity")
        print("7. Exit")

    def analyzer_operations(self):
        try:
            self.analyzer_menu()
            while True:
                choice = input("Enter your choice: ").strip()
                if choice == "1":
                    self.analyzer.get_summary()
                elif choice == "2":
                    self.analyzer.get_hottest_day()
                elif choice == "3":
                    self.analyzer.get_coldest_day()
                elif choice == "4":
                    self.analyzer.get_total_rainfall()
                elif choice == "5":
                    self.analyzer.get_average_temperature()
                elif choice == "6":
                    self.analyzer.get_average_humidity()
                elif choice == "7":
                    print("Exiting ...")
                    break
                else:
                    print("Invalid choice. Please try again.")

        except Exception as e:
            print(f"Error analyzing CSV: {e}")

    def run(self):
        try:
            while True:
                self.display_menu()
                choice = input("Enter your choice: ").strip()

                if choice == "1":
                    self.load_file()
                elif choice == "2":
                    self.analyze_data()
                elif choice == "3":
                   self.generate_report()
                elif choice == "4":
                    self.visualize_data()
                elif choice == "5":
                    print("Exiting program...")
                    break
                else:
                    print("Invalid choice. Please try again.")
        except KeyboardInterrupt as e:
            print(f"Exiting program... {e}")


    def load_file(self):
        files = self.reader.list_csv_files()
        if not files:
            print("No CSV files found.")
            print("-" * 30)
            return

        print("Available CSV files:")
        print("=" * 30)
        for i, f in enumerate(files, start=1):
            print(f"{i}. {f}")

        choice = input("Enter file number: ").strip()
        print("=" * 30)
        try:
            index = int(choice) - 1
            file_name = files[index]
            rows = self.reader.read_csv(file_name)
            data = process_data(rows)
            self.analyzer.processed_data.extend(data)
            print("Loading csv data...")
            print(f"\nLoaded {len(rows)} records from {file_name}")
            print("------------------------------\n\n")

        except (ValueError, IndexError):
            print("Invalid selection.")

    def analyze_data(self):
        """ Analyze data and generate summary """
        try:
            summary = self.analyzer.get_summary()
            print("-- Summary of data: --")
            print("=" * 30)
            for key, value in summary.items():
                print(f"{key}: {value}")
            print("=" * 30)
            while True:
                print("If you want to do more analysis(Yes/No) ? ")
                print("=" * 30)
                choice = input("Enter your choice: ").strip().lower()
                if choice == "yes":
                   self.analyzer_operations()
                elif choice == "no":
                    print("Going to main menu ...")
                    print("=" * 30)
                    break
                else:
                    print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"Error analyzing CSV: {e}")

    def generate_report(self):
        """Generate a human-readable report."""
        try:
            report_gen = ReportGenerator(self.analyzer)
            print("=" * 30)
            print("-- Generate report  --.")
            print("1. Generate txt report.\n2. Generate JSON summary.")
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                report_gen.generate_report()
            elif choice == "2":
                report_gen.generate_json_summary()
            else:
                print("Invalid choice. Please try again.")
            print("=" * 30)

        except Exception as e:
            print(f"Error generating report: {e}")

    def visualize_data(self):
        """Generate visual graphs from processed data."""
        try:
            if not self.analyzer.processed_data:
                print("No data available. Please read and analyze CSV first.")
                return

            visualizer = DataVisualizer(self.analyzer.processed_data)

            print("-- Visualization Menu --")
            print("=" * 30)
            print("1. Plot temperature trend")
            print("2. Plot humidity trend")
            print("3. Plot rainfall pattern")
            print("4. Back to main menu")
            print("=" * 30)

            while True:
                choice = input("Enter your choice: ").strip()
                if choice == "1":
                    visualizer.plot_temperature_trend()
                elif choice == "2":
                    visualizer.plot_humidity_trend()
                elif choice == "3":
                    visualizer.plot_rainfall_trend()
                elif choice == "4":
                    print("Returning to main menu...")
                    break
                else:
                    print("Invalid choice. Please try again.")

        except Exception as e:
            print(f"Error generating visualization: {e}")
