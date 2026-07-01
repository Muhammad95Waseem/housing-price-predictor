---
title: Housing Price Predictor
emoji: 🏠
colorFrom: blue
colorTo: green
sdk: docker
app_port: 7860
---

**Hugging Face Spaces deployment:** Create a Space on Hugging Face and push the project folder there, it will start building and start the app. then check app in app sction.

# California Housing Price Predictor

A simple Machine Learning web application built with Flask that predicts house prices using the California Housing dataset.

The application automatically trains a model on the first run, saves the trained model and preprocessing pipeline as pickle files, and uses them for future predictions.

---

## Features

- Web interface built with Flask
- Automatic model training on first execution
- Saved model reuse on subsequent runs
- Data preprocessing using Scikit-Learn Pipelines
- Numerical imputation and standardization
- One-hot encoding for categorical features
- Random Forest Regressor for prediction
- Interactive housing price prediction form

---

## Dataset Features

| Feature | Description |
|---------|-------------|
| longitude | Longitude coordinate |
| latitude | Latitude coordinate |
| housing_median_age | Median age of houses |
| total_rooms | Total number of rooms |
| total_bedrooms | Total number of bedrooms |
| population | Population in the block |
| households | Number of households |
| median_income | Median income |
| ocean_proximity | Proximity to the ocean |

### Target Variable

`median_house_value`

---

## Project Structure

```text
housing-price-predictor/

├── data
│   └── housing.csv

├── model/
│   ├── model.pkl
│   └── pipeline.pkl

├── templates/
│   └── index.html

└── static/
    └── style.css

├── app.py
├── requirements.txt
├── README.md

```

---

## Tech Stack

![Python](https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Joblib](https://img.shields.io/badge/joblib-4479A1?style=for-the-badge&logo=python&logoColor=white)

---

## Installation

Clone the repository

```bash
git clone https://github.com/your_username/housing-price-predictor.git
```

Move into the project directory

```bash
cd housing-price-predictor
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the Flask application

```bash
python app.py
```

### First Run

When the application is executed for the first time:

- `housing.csv` is loaded
- The preprocessing pipeline is created
- The Random Forest model is trained
- `model.pkl` is generated
- `pipeline.pkl` is generated
- The Flask web server starts automatically

### Subsequent Runs

If the pickle files already exist:

- The model and pipeline are loaded directly
- No retraining is performed
- Predictions are available immediately

---

## Sample Input

| Feature | Value |
|---------|-------|
| longitude | -122.23 |
| latitude | 37.88 |
| housing_median_age | 41 |
| total_rooms | 880 |
| total_bedrooms | 129 |
| population | 322 |
| households | 126 |
| median_income | 8.3252 |
| ocean_proximity | NEAR BAY |

Expected house value:

```text
452600
```

---

## Future Improvements

- Separate training and inference scripts
- Deploy on Render
- Add Docker support
- Improve UI styling
- Display feature importances
- Add model evaluation metrics

---

## Author

**Muhammad Waseem Channa**

Aspiring Data Scientist and Machine Learning Engineer