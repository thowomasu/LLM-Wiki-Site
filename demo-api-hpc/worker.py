import csv
import json
import sys
from pathlib import Path


def read_rows(path):
    with Path(path).open(newline="") as handle:
        return list(csv.DictReader(handle))


def to_float(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def summarize(input_csv):
    rows = read_rows(input_csv)
    currents = [to_float(row.get("current_a")) for row in rows]
    voltages = [to_float(row.get("voltage_v")) for row in rows]
    temperatures = [to_float(row.get("temperature_c")) for row in rows]

    currents = [value for value in currents if value is not None]
    voltages = [value for value in voltages if value is not None]
    temperatures = [value for value in temperatures if value is not None]

    if not rows:
        raise ValueError("input CSV has no data rows")

    return {
        "rows": len(rows),
        "current_a": {
            "min": min(currents) if currents else None,
            "max": max(currents) if currents else None,
            "mean": sum(currents) / len(currents) if currents else None,
        },
        "voltage_v": {
            "min": min(voltages) if voltages else None,
            "max": max(voltages) if voltages else None,
            "mean": sum(voltages) / len(voltages) if voltages else None,
        },
        "temperature_c": {
            "min": min(temperatures) if temperatures else None,
            "max": max(temperatures) if temperatures else None,
            "mean": sum(temperatures) / len(temperatures) if temperatures else None,
        },
    }


def main():
    if len(sys.argv) != 3:
        raise SystemExit("usage: python worker.py <input_csv> <output_json>")

    input_csv = Path(sys.argv[1])
    output_json = Path(sys.argv[2])
    output_json.parent.mkdir(parents=True, exist_ok=True)

    result = summarize(input_csv)
    result["input_csv"] = str(input_csv)
    result["status"] = "finished"

    output_json.write_text(json.dumps(result, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
