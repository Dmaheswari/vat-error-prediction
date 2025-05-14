
# VAT Error Prediction Project

This project is a machine learning-based web application for predicting VAT discrepancies. It takes user inputs such as Amount, VAT Rate, Expected VAT, VAT Diff, Country, and Item Category to predict VAT error.

## Features
- User-friendly form to input data.
- Predict VAT errors using a trained machine learning model.
- Supports multiple countries and item categories.
- Built using Flask for the web backend and trained with a machine learning model.

## Project Structure
The project contains two main parts:
1. **Flask Web Application**: 
   - A simple web interface that allows users to input data and receive predictions.
   - The Flask app exposes a `/predict` API endpoint that accepts POST requests containing the user's data and returns the VAT prediction.
   
2. **Machine Learning Model**: 
   - A trained model (`vat_error_model.joblib`) that predicts VAT errors based on the input data.
   - The model is loaded in the Flask app to make predictions.

## How to Run

### 1. Set up the Environment

Clone this repository:

```bash
git clone https://github.com/yourusername/vat-error-prediction.git
cd vat-error-prediction
```

Install the necessary Python dependencies:

```bash
pip install -r requirements.txt
```

### 2. Run the Flask App

Start the Flask web server:

```bash
python app.py
```

The Flask server will be running at `http://127.0.0.1:5000`.

### 3. Use the Web Interface

Open the HTML file `index.html` in a browser.

- Fill out the form with the appropriate values.
- Click "Predict" to see the VAT error prediction.
  
### 4. Test the API Directly

You can also use Postman or any API client to make a POST request to:

```http
POST http://127.0.0.1:5000/predict
```

Send a JSON body with the following data structure:

```json
[
  {
    "Amount": 1000,
    "VAT_Rate": 28,
    "Expected_VAT": 30,
    "VAT_Diff": 20,
    "Country_Germany": 0,
    "Country_India": 1,
    "Country_Norway": 0,
    "Country_UK": 0,
    "Item_Category_Books": 0,
    "Item_Category_Clothing": 1,
    "Item_Category_Electronics": 0,
    "Item_Category_Food": 0
  }
]
```

The response will be a prediction value.

## Dependencies

- Flask
- pandas
- joblib

To install the dependencies, run:

```bash
pip install -r requirements.txt









