from datetime import datetime

def process_data(raw_data):
    """Clean and normalize CSV data."""
    processed = []
    for row in raw_data:
        try:
            processed.append({
                "date": datetime.strptime(row["date"], "%Y-%m-%d"),
                "temperature": float(row["temperature"]),
                "humidity": float(row["humidity"]),
                "rainfall": float(row["rainfall"]),
                "condition": row.get("condition", "").strip().capitalize()
            })
        except (ValueError, KeyError):
            # Skip bad rows
            continue
    return processed
