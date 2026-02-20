# F1 Lap Time Prediction (FP → Qualifying)

Machine learning model that predicts Formula 1 qualifying lap times using Free Practice session data.

## Overview

This project explores whether Free Practice telemetry can predict qualifying performance.

Using FastF1 API data, a regression model is trained on Free Practice laps and used to estimate each driver’s expected qualifying lap time and predicted grid order.

The project evaluates:
- Lap time prediction accuracy
- Predicted vs real qualifying order
- Position change analysis

## Example Result — Australia 2025

The model predicts qualifying lap times and grid positions.

Metrics:
- Mean Absolute Error ≈ 0.84 sec
- Grid prediction differences analyzed per driver

Key insight:
The model captures team performance and general pace but struggles with final Q3 peak laps.

## Visualizations

- Predicted vs Real Lap Times
- Net Position Change
- Feature Importance (Random Forest)
  
## Structure/Steps

Data source:
- FastF1 telemetry

Preprocessing:
- Filter clean laps
- Remove traffic / yellow flags
- Lap time threshold filtering
- One-hot encoding (driver, team, compound)

Model:
- Random Forest Regressor

Strategy:
1. Train on Free Practice laps
2. Predict lap times per lap
3. Aggregate top predicted laps per driver
4. Produce predicted qualifying order

## Setup

Clone repo:

git clone https://github.com/Joeescobar87/f1-lap-prediction-ml

Create environment:

python3 -m venv .venv
source .venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Run notebook:

src/train.ipynb

## Future Work

- Tire degradation modeling
- Race pace simulation
- Pit strategy modeling
- Deep learning approaches
