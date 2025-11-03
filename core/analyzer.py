
from statistics import mean

class CsvAnalyzer:
    def __init__(self):
        self.raw_data = []
        self.processed_data = []
        self.summary = {}


    def get_summary(self):
        """Compute averages and find extreme days."""

        try:
            temps = [float(row["temperature"]) for row in self.processed_data]
            hums = [float(row["humidity"]) for row in self.processed_data]
            rains = [float(row["rainfall"]) for row in self.processed_data]

            hottest = max(self.processed_data, key=lambda x: float(x["temperature"]))
            coldest = min(self.processed_data, key=lambda x: float(x["temperature"]))

            self.summary = {
                "average_temperature": round(mean(temps), 2),
                "average_humidity": round(mean(hums), 2),
                "total_rainfall": round(sum(rains), 2),
                "hottest_day": (hottest["date"], hottest["temperature"]),
                "coldest_day": (coldest["date"], coldest["temperature"])
            }

            return self.summary

        except Exception as e:
            print(f"Error analyzing CSV: {e}")
            return {}

    def get_hottest_day(self):
        try:
            print("-- Hottest Day --")
            print("=" *30)
            result = self.summary["hottest_day"]
            print(f"The hottest day is: {result} ")
        except Exception as e:
            print(f"Error getting hottest day: {e}")
            return ""

    def get_coldest_day(self):
        try:
            print("-- Coldest Day --")
            print("=" * 30)
            result = self.summary["coldest_day"]
            print(f"The Coldest Day is: {result} ")
        except Exception as e:
            print(f"Error getting hottest day: {e}")
            return ""

    def get_total_rainfall(self):
        try:
            print("-- Total Rainfall --")
            print("=" * 30)
            result = self.summary["total_rainfall"]
            print(f"The Total Rainfall is: {result} ")
        except Exception as e:
            print(f"Error getting hottest day: {e}")
            return ""

    def get_average_temperature(self):
        try:
            print("-- Average Temperature --")
            print("=" * 30)
            result = self.summary["average_temperature"]
            print(f"The Average Temperature is: {result} ")
        except Exception as e:
            print(f"Error getting hottest day: {e}")
            return ""

    def get_average_humidity(self):
        try:
            print("-- Average Humidity  --")
            print("=" * 30)
            result = self.summary["average_humidity"]
            print(f"The Average Humidity is: {result} ")
        except Exception as e:
            print(f"Error getting hottest day: {e}")
            return ""

