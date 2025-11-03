# core/report.py
import json
from datetime import datetime, date
from utils.paths import get_output_path

class ReportGenerator:
    """Handles report creation in text and JSON formats."""

    def __init__(self, analyzer):
        self.analyzer = analyzer
        self.text_path = get_output_path("report.txt")
        self.json_path = get_output_path("report.json")


    def generate_report(self):
        """Generate a human-readable text report."""
        try:
            summary = self.analyzer.get_summary()
            report_content = self._format_text_report(summary)

            # Use Path’s write_text() for simplicity and UTF-8 safety
            self.text_path.write_text(report_content, encoding="utf-8")
            print(f"\nReport generated successfully at {self.text_path}")

        except Exception as e:
            print(f"Error generating report: {e}")



    def generate_json_summary(self):
        """Generate a JSON version of the summary for external systems."""
        try:
            summary = self.analyzer.get_summary()

            def default_serializer(obj):
                if isinstance(obj, (datetime, date)):
                    return obj.isoformat()
                return str(obj)

            self.json_path.write_text(
                json.dumps(summary, indent=4, default=default_serializer),
                encoding="utf-8"
            )
            print(f"JSON summary saved to {self.json_path}")
        except Exception as e:
            raise FileNotFoundError(f"Error saving JSON summary: {e}")

    def _format_text_report(self, summary):
        """Private helper to format text report."""
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        report = [
            "=" * 50,
            "          WEATHER DATA REPORT",
            "=" * 50,
            f"Generated on: {now}",
            "-" * 50,
            f"Average Temperature: {summary['average_temperature']}°C",
            f"Average Humidity: {summary['average_humidity']}%",
            f"Total Rainfall: {summary['total_rainfall']} mm",
            f"Hottest Day: {summary['hottest_day'][0]} ({summary['hottest_day'][1]}°C)",
            f"Coldest Day: {summary['coldest_day'][0]} ({summary['coldest_day'][1]}°C)",
            f"\n" + "-" * 50,
            "NOTE",
            "-" * 50,
            "Report generated automatically by Weather Data Visualizer v2."
        ]
        return "\n".join(report)
