import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

print("Generating synthetic industrial sensor dataset...")
np.random.seed(42)
n_samples = 1000

vibration = np.random.uniform(0.5, 8.0, n_samples)
temperature = np.random.uniform(40.0, 95.0, n_samples)
current = np.random.uniform(10.0, 35.0, n_samples)

# Rule for status: 1 if vibration > 5.5 or temp > 80 or current > 28, else 0
status = []
for v, t, c in zip(vibration, temperature, current):
    if v > 5.5 or t > 80.0 or c > 28.0:
        status.append(1)
    else:
        status.append(0)

df = pd.DataFrame({
    'vibration': vibration,
    'temperature': temperature,
    'current': current,
    'status': status
})

df.to_csv('industrial_sensor_data.csv', index=False)
print("Dataset saved as 'industrial_sensor_data.csv'.")

X = df[['vibration', 'temperature', 'current']]
y = df['status']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training Random Forest Classifier...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)
print(f"Model Training Complete! Accuracy: {accuracy * 100:.2f}%")

joblib.dump(model, 'model.joblib')
print("Model artifact saved as 'model.joblib'.")
