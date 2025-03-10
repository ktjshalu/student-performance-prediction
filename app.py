from flask import Flask, request, render_template, jsonify
import numpy as np
import pandas as pd
import logging

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application

# Configure logging
logging.basicConfig(level=logging.DEBUG)

## Route for a home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        try:
            data = CustomData(
                gender=request.form.get('gender'),
                race_ethnicity=request.form.get('ethnicity'),
                parental_level_of_education=request.form.get('parental_level_of_education'),
                lunch=request.form.get('lunch'),
                test_preparation_course=request.form.get('test_preparation_course'),
                reading_score=float(request.form.get('writing_score')),
                writing_score=float(request.form.get('reading_score'))
            )
            pred_df = data.get_data_as_data_frame()
            logging.debug(f"DataFrame: {pred_df}")
            logging.debug("Before Prediction")

            predict_pipeline = PredictPipeline()
            logging.debug("Mid Prediction")
            results = predict_pipeline.predict(pred_df)
            logging.debug(f"Prediction Results: {results}")
            logging.debug("After Prediction")
            return render_template('home.html', results=results[0])
        except Exception as e:
            logging.error(f"Error during prediction: {e}")
            return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 5000  # Change this if needed

    # Start the Flask app
    app.run(host=host, port=port, debug=True)
