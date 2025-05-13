"""
Run the WBWAI metric‑suite after being triggered by repository_dispatch.
Usage: python inference.py
"""
import os
import csv
import json
from datetime import datetime

CSV_HEADER = ["name", "correct", "incorrect", "total", "accuracy", "tokenCount"]

def gen_metric():
    print("Generating metric based on inference results")
    rows = [CSV_HEADER]
    for filename in os.listdir("./results/inference"):
        correct = 0
        incorrect = 0
        token_count = 0
        print(f"Metric result for {filename}")
        results = {}
        ground_truths = {}
        with open(os.path.join("./results/inference", filename), "r") as file:
            for line in file:
                data = json.loads(line)
                results[data["name"]] = data["result"]
                token_count += data["tokenCount"]
        with open(os.path.join("./results/ground_truth", filename), "r") as file:
            for line in file:
                data = json.loads(line)
                ground_truths[data["name"]] = data["ground_truth"]

        for name, result in results.items():
            if name in ground_truths and result == ground_truths[name]:
                correct += 1
            else:
                incorrect += 1
        rows.append([filename.split(".")[0], correct, incorrect, correct + incorrect, correct / (correct + incorrect) if (correct + incorrect) > 0 else 0, token_count])

        output_filename = f"{filename.split('.')[0]}_metric_{datetime.now().strftime('%m%d%H%M')}.csv"
        with open(os.path.join("./results/metric", output_filename), "w+") as file:
            writer = csv.writer(file)
            writer.writerows(rows)
    print(f"Metric generation completed, results are saved in ./results/{output_filename}")

if __name__ == "__main__":
    print("Directly generating metric")
    gen_metric()
