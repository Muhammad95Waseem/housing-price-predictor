from flask import Flask, render_template, request
import pandas as pd
import joblib
import numpy as np
import os
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor

MODEL_FILE = "model/model.pkl"
PIPELINE_FILE = "model/pipeline.pkl"

def build_pipeline(num_attribs, cat_attribs):
    
    num_pipeline = Pipeline([
    ("Imput", SimpleImputer(strategy="median")),
    ("Standerdization", StandardScaler())
    ])

    cat_pipeline = Pipeline([
    ("Encod", OneHotEncoder(handle_unknown='ignore'))
    ])

    final_pipeline = ColumnTransformer([
    ("num", num_pipeline, num_attribs),
    ("cat", cat_pipeline, cat_attribs)
    ])

    return final_pipeline

if not os.path.exists(MODEL_FILE):

    housing = pd.read_csv("data/housing.csv")
    housing['income_cat'] = pd.cut(housing["median_income"], 
                                   bins=[0.0, 1.5, 3.0, 4.5, 6.0, np.inf], 
                                   labels=[1, 2, 3, 4, 5])
    split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
    for train_index, _ in split.split(housing, housing['income_cat']):
        housing_train = housing.loc[train_index].drop("income_cat", axis=1)
        
 
    housing_labels = housing_train["median_house_value"].copy()
    housing_features = housing_train.drop("median_house_value", axis=1)
 
    num_attribs = housing_features.drop("ocean_proximity", axis=1).columns.tolist()
    cat_attribs = ["ocean_proximity"]
 
    pipeline = build_pipeline(num_attribs, cat_attribs)
    housing_prepared = pipeline.fit_transform(housing_features)
 
    model = RandomForestRegressor(random_state=42)
    model.fit(housing_prepared, housing_labels)
 
    # Save model and pipeline
    joblib.dump(model, MODEL_FILE)
    joblib.dump(pipeline, PIPELINE_FILE)
 
print("Model trained and saved.")


app = Flask(__name__)

# Load trained objects
model = joblib.load("model/model.pkl")
pipeline = joblib.load("model/pipeline.pkl")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():

    try:

        data = {
            'longitude': float(request.form['longitude']),
            'latitude': float(request.form['latitude']),
            'housing_median_age': int(request.form['housing_median_age']),
            'total_rooms': int(request.form['total_rooms']),
            'total_bedrooms': int(request.form['total_bedrooms']),
            'population': int(request.form['population']),
            'households': int(request.form['households']),
            'median_income': float(request.form['median_income']),
            'ocean_proximity': request.form['ocean_proximity']
        }

        input_df = pd.DataFrame([data])
        transformed_data = pipeline.transform(input_df)
        prediction = model.predict(transformed_data)
        predicted_price = round(prediction[0], 2)

        return render_template('index.html', prediction=predicted_price)

    except Exception as e:

        return render_template('index.html', prediction=f"Error: {e}")


if __name__ == '__main__':
    app.run(debug=True)