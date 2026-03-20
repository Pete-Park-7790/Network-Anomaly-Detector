# AI-Powered Network Anomaly Detector 🛡️

## Overview
A lightweight, machine-learning-based Intrusion Detection System (IDS) designed to analyze network traffic and identify malicious behavior (like DDoS, port scans, and fuzzing) in real-time. 

Unlike traditional signature-based firewalls, this tool uses **Unsupervised Machine Learning** to establish a baseline of normal network behavior and mathematically isolate anomalous traffic without requiring predefined threat signatures.

## Architecture
To simulate enterprise-grade security software, this project is decoupled into two distinct pipelines:
1. **The Model Trainer (`analyzer.py`):** Ingests massive network datasets, cleans the features using Pandas, and trains an `Isolation Forest` algorithm. It exports the trained mathematical model as a serialized `.pkl` file.
2. **The Inference Engine (`scanner.py`):** A high-speed scanning script that loads the pre-trained brain and evaluates new, unseen network traffic, generating an automated incident report (`live_threats_caught.csv`).

## Tech Stack
* **Language:** Python 3.x
* **Machine Learning:** `scikit-learn` (Isolation Forest)
* **Data Engineering:** `pandas`
* **Model Serialization:** `joblib`

## Dataset
This model is configured to train on modern cybersecurity datasets such as **NSL-KDD**. It processes numerical network features including connection durations, byte transfers, and protocol error rates.

## How to Run Locally

### 1. Install Dependencies
Ensure Python is installed, then run:
`pip install pandas scikit-learn joblib`

### 2. Train the AI Brain
Place your training dataset (e.g., `NSL-KDDTest+.txt`) in the root directory.
`python analyzer.py`
*(This will generate an `ai_brain.pkl` file).*

### 3. Scan for Threats
Place your testing dataset in the root directory to simulate live traffic.
`python scanner.py`
Replace the file name at line 17 with your test file name.
*(This will output a `live_threats_caught.csv` file containing all isolated attacks).*

## Why Isolation Forest?
For a local, lightweight security tool, standard neural networks are too computationally expensive and slow for real-time packet analysis. Isolation Forest is highly efficient at identifying mathematical outliers in high-dimensional datasets, making it perfect for rapid anomaly detection on standard hardware.
