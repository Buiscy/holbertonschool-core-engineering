#!/usr/bin/env python3
import csv
import json


def convert_csv_to_json(filename):

    try:
        with open(filename, "r", newline="") as file:
            read = csv.DictReader(file)
            rows = list(read)

    except Exception:
        return False

    try:
        with open("data.json", "w") as files:
            json.dump(rows, files)
            return True
    except Exception:
        return False
