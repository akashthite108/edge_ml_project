from flask import Flask, jsonify, request
import joblib
import numpy as np

app = Flask(__name__)

# Load trained Random Forest model (ensure model.joblib is in the same directory)
try:
    model = joblib.load('model.joblib')
except Exception as e:
    model = None
    print(f"Warning: Model could not be loaded: {e}")

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify(status="healthy", service="edge-ml-scoring-module"), 200

@app.route('/score', methods=['POST'])
def score():
    if model is None:
        return jsonify(error="Model not loaded"), 500
    
    data = request.get_json(force=True)
    try:
        vibration = float(data.get('vibration', 0.0))
        temperature = float(data.get('temperature', 0.0))
        current = float(data.get('current', 0.0))
        
        # Features array
        features = np.array([[vibration, temperature, current]])
        prediction = int(model.predict(features)[0])
        probability = float(np.max(model.predict_proba(features)))
        
        status_text = "Anomaly / Failure Imminent" if prediction == 1 else "Normal Operation"
        
        result = {
            "prediction": prediction,
            "status": status_text,
            "confidence": round(probability * 100, 2),
            "telemetry": {
                "vibration": vibration,
                "temperature": temperature,
                "current": current
            }
        }
        return jsonify(result), 200
    except Exception as e:
        return jsonify(error=str(e)), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
