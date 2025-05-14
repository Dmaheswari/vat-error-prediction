# from flask import Flask, request, jsonify
# import joblib
# import pandas as pd

# app = Flask(__name__)

# # Load the saved model
# try:
#     model = joblib.load('vat_error_model.joblib')
# except Exception as e:
#     print("Error loading model:", e)
#     model = None

# @app.route('/')
# def home():
#     return "VAT Error Model API is running."

# @app.route('/predict', methods=['POST'])
# def predict():
#     if model is None:
#         return jsonify({'error': 'Model could not be loaded'}), 500

#     try:
#         data = request.get_json()

#         # Convert to DataFrame
#         df = pd.DataFrame(data)

#         # Optional: Check if necessary columns are present
#         # Replace ['feature1', 'feature2', ...] with your real feature names
#         required_columns = model.feature_names_in_.tolist()
#         if not all(col in df.columns for col in required_columns):
#             return jsonify({'error': 'Missing one or more required features'}), 400

#         prediction = model.predict(df)
#         return jsonify({'prediction': prediction.tolist()})
    
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask, request, jsonify
# import joblib
# import pandas as pd
# import time

# app = Flask(__name__)

# # Load the saved model
# try:
#     model = joblib.load('vat_error_model.joblib')
#     print("Model loaded successfully.")
#     print("Expected features:", model.feature_names_in_)
# except Exception as e:
#     print("Error loading model:", e)
#     model = None

# @app.route('/')
# def home():
#     return "VAT Error Model API is running."

# @app.route('/predict', methods=['POST'])
# def predict():
#     if model is None:
#         return jsonify({'error': 'Model could not be loaded'}), 500

#     try:
#         data = request.get_json()

#         # Convert to DataFrame
#         df = pd.DataFrame(data)

#         # Check if all required features are present
#         required_columns = model.feature_names_in_.tolist()
#         missing = [col for col in required_columns if col not in df.columns]
#         if missing:
#             return jsonify({'error': f'Missing required features: {missing}'}), 400

#         # Measure prediction time
#         start = time.time()
#         prediction = model.predict(df)
#         duration = round(time.time() - start, 3)

#         return jsonify({
#             'prediction': prediction.tolist(),
#             'time_taken': f"{duration} seconds"
#         })
    
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# if __name__ == '__main__':
#     # Flask's debug mode is good for development, not production
#     app.run(debug=True, host='0.0.0.0', port=5000)




from flask import Flask, request, jsonify
import joblib
import pandas as pd
from flask_cors import CORS

# Initialize Flask app and CORS
app = Flask(__name__)
CORS(app)  # This will allow cross-origin requests

# Load the saved model
try:
    model = joblib.load('vat_error_model.joblib')  # Adjust the path if needed
except Exception as e:
    print("Error loading model:", e)
    model = None

@app.route('/')
def home():
    return "VAT Error Model API is running."

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Model could not be loaded'}), 500

    try:
        # Get JSON data from the request
        data = request.get_json()
        print("Received data:", data)

        # Convert to DataFrame
        df = pd.DataFrame(data)

        # Check if necessary columns are present
        required_columns = model.feature_names_in_.tolist()
        if not all(col in df.columns for col in required_columns):
            return jsonify({'error': 'Missing one or more required features'}), 400

        # Make prediction using the model
        prediction = model.predict(df)
        print("Prediction:", prediction)

        # Return the prediction in the response
        return jsonify({'prediction': prediction.tolist()})

    except Exception as e:
        print("Error:", e)  # Log the error for debugging
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
