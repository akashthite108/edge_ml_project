import time
import random
import requests
import json

URL = 'http://localhost:5001/score'

print("Starting IoT Sensor Data Simulator...")
print("Streaming telemetry to edge scoring endpoint. Press Ctrl+C to stop.\n")

try:
    while True:
        # Simulate live sensor readings (mix of normal and abnormal conditions)
        is_anomaly = random.random() < 0.25 # 25% chance of anomaly for testing
        
        if is_anomaly:
            vibration = round(random.uniform(5.5, 8.5), 2)
            temperature = round(random.uniform(80.0, 95.0), 2)
            current = round(random.uniform(28.0, 38.0), 2)
        else:
            vibration = round(random.uniform(1.0, 4.0), 2)
            temperature = round(random.uniform(45.0, 70.0), 2)
            current = round(random.uniform(12.0, 22.0), 2)
            
        payload = {
            "vibration": vibration,
            "temperature": temperature,
            "current": current
        }
        
        try:
            response = requests.post(URL, json=payload, timeout=3)
            print(f"Payload Sent: {payload}")
            print(f"Edge Response: {response.json()}\n")
        except requests.exceptions.ConnectionError:
            print("Error: Could not connect to edge scoring module. Make sure Docker container is running on port 5001.")
        
        time.sleep(5)
except KeyboardInterrupt:
    print("\nSimulator stopped by user.")
