# WBW Monitor

This repo will actively monitor changes in the WBWAI Repo. Any new commit in the following branches will trigger an metric evaluation (`main`, `prod`, `dev1`).

## Dataset

Too add a dataset, please add the correctly formatted json under `input/{test_name}.json`. 

If metric evaluation (accuracy validation) is needed, you can also include the expected answer/ground_truth in `results/ground_truth/{test_name}.json`.

Examples are provided in the folders as `example.json`

## Inference

During inference, functions will call appropriate WBWAI's API to generate corresponding inference. `inference.py` will be the entrypoint of the inference stage.

All inference results will be saved in `results/inference/{test_name}.json`

## Metric Generation

After running model inference, metric will be generated in `metric.py`, the script will validate the inference result with the given ground truth to evaluate the model's performance of accuracy and token count.

