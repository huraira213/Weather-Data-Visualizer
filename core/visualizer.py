# core/visualizer.py
import matplotlib.pyplot as plt
from utils.paths import get_output_path

class DataVisualizer:
    """Handles creating visual plots for weather data."""

    def __init__(self, data):
        self.data = data

    def _save_plot(self, plt_obj, filename):
        path = get_output_path(filename)
        plt_obj.tight_layout()
        plt_obj.savefig(path)
        plt_obj.close()
        print(f" Saved: {path}")

    def plot_temperature_trend(self):
        dates = [row["date"] for row in self.data]
        temps = [float(row["temperature"]) for row in self.data]

        plt.figure(figsize=(8, 4))
        plt.plot(dates, temps, marker="o", color="orange", label="Temperature (°C)")
        plt.title("Temperature Trend")
        plt.xlabel("Date")
        plt.ylabel("Temperature (°C)")
        plt.legend()
        plt.xticks(rotation=45)
        self._save_plot(plt, "temperature_trend.png")

    def plot_humidity_trend(self):
        dates = [row["date"] for row in self.data]
        hum = [float(row["humidity"]) for row in self.data]

        plt.figure(figsize=(8, 4))
        plt.plot(dates, hum, marker="s", color="blue", label="Humidity (%)")
        plt.title("Humidity Trend")
        plt.xlabel("Date")
        plt.ylabel("Humidity (%)")
        plt.legend()
        plt.xticks(rotation=45)
        self._save_plot(plt, "humidity_trend.png")

    def plot_rainfall_trend(self):
        dates = [row["date"] for row in self.data]
        rain = [float(row["rainfall"]) for row in self.data]

        plt.figure(figsize=(8, 4))
        plt.bar(dates, rain, color="teal")
        plt.title("Rainfall Pattern")
        plt.xlabel("Date")
        plt.ylabel("Rainfall (mm)")
        plt.xticks(rotation=45)
        self._save_plot(plt, "rainfall_pattern.png")
