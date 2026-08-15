from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load your trained model and scaler
model = joblib.load('/home/sha/mysite/models/nids_rf.pkl')
scaler = joblib.load('/home/sha/mysite/models/scaler.pkl')

@app.route('/')
def home():
    return "NIDS Model API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = np.array(data['features']).reshape(1, -1)
    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled)
    return jsonify({'prediction': str(prediction[0])})

if __name__ == '__main__':
    app.run()
