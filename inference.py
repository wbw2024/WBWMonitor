"""
Run the WBWAI inference‑suite after being triggered by repository_dispatch.
Usage: python inference.py
"""

import os
import json

def get_example_result(name):
    answers = {
        "example_1": {"answer": "Hi there! How can I help you today?", "tokenCount": 10},
        "example_2": {"answer": "Testing 1 2 3", "tokenCount": 8},
    }
    return answers.get(name, "No answer found")

def gen_inference():
    print("Generating inference results")
    for filename in os.listdir("./input"):
        print(f"Inference result for {filename}")
        results = []
        with open(os.path.join("./input", filename), "r") as file:
            for line in file:
                data = json.loads(line)
                # Simulate some inference processing
                result = get_example_result(data["name"])
                results.append({
                    "name": data["name"],
                    "package": data["package"],
                    "api": data["api"],
                    "tokenCount": result["tokenCount"],
                    "result": result["answer"],
                })
        with open(os.path.join("./results/inference", filename), "w+") as file:
            for result in results:
                file.write(json.dumps(result) + "\n")
    print("Inference results generated")

if __name__ == "__main__":
    gen_inference()
    print("Running inference.py directly")

