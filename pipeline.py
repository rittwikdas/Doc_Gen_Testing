import time
import random

def step_log(step_name):
    print(f"[STEP] Running: {step_name}")
    time.sleep(0.2)  # Simulate time delay

def run_pipeline():
    steps = [
        "Load data from 15 CSVs",
        "Normalize and transform 100+ features",
        "Generate 25 engineered features",
        "Split dataset into 80/20",
        "Train model on 100,000 rows",
        "Evaluate model using 10 metrics",
        "Push model to registry",
        "Deploy model to staging"
    ]
    for step in steps:
        step_log(step)
    print("[PIPELINE] All steps completed.")
