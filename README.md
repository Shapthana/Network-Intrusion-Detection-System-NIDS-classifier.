# Network Intrusion Detection System (NIDS)

A machine learning classifier that detects malicious vs. normal network traffic, trained on the NSL-KDD dataset and deployed as a live cloud API.

## Overview
This project builds a binary classifier (normal vs. attack) using network traffic features such as protocol type, service, byte counts, and connection statistics. The trained model is deployed as a REST API that accepts traffic feature data and returns real-time predictions.

## Dataset
[NSL-KDD](https://www.kaggle.com/datasets/hassan06/nslkdd) — a well-known benchmark dataset for network intrusion detection, containing 41 traffic features across 125,973 training records and 22,544 test records.

## Approach
1. Preprocessed the data: encoded categorical features (protocol type, service, flag), scaled numeric features
2. Trained and compared three models: Random Forest, Gradient Boosting, and class-weighted Random Forest
3. Evaluated on NSL-KDD's official test set, which intentionally includes attack types unseen during training

## Results
| Model | Accuracy | Attack Recall |
|---|---|---|
| Random Forest | 78% | 0.64 |
| Gradient Boosting | 79% | 0.65 |
| Random Forest (balanced) | 77% | 0.62 |

The ~78% accuracy ceiling reflects a known challenge of the NSL-KDD test set: it deliberately includes attack types not present in training, testing a model's ability to generalize to novel threats rather than memorize known signatures.

## Deployment
The trained model is deployed as a Flask API, accepting POST requests with 41 traffic features and returning a prediction (`normal` or `attack`).

Example request:
```bash
curl -X POST https://sha.pythonanywhere.com/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [0,1,20,9,491,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,2,2,0,0,0,0,1,0,0,150,25,0.17,0.03,0.17,0,0,0,0,0,0]}'
```

## Tech Stack
Python, pandas, scikit-learn, Flask, PythonAnywhere (cloud deployment)
