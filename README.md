# Real-Time ML Application Using Azure Machine Learning and IoT Edge

**Student Name:** Akash Thite  
**Enrollment No:** ADT23SOCB0092  
**Class & Division:** LY AIEC-02 | **Roll No:** 02  

---

## Project Overview
This repository contains the complete source code and configuration files for the **AIEC Mini Project** implementing an Industrial IoT (IIoT) edge architecture. It captures real-time sensor telemetry (vibration, temperature, and current), performs local machine learning inference using a trained Random Forest classifier, and detects machinery anomalies instantly at the edge.

---

## Repository File Structure
- `train_model.py`: Generates synthetic sensor data and trains the Random Forest classifier (`model.joblib`).
- `app.py`: Flask web server providing the edge scoring endpoint (`/score`).
- `simulate_sensor.py`: Python simulator that streams live sensor telemetry to the edge module.
- `requirements.txt`: Python package dependencies.
- `Dockerfile`: Container configuration for packaging the edge ML module.

---

## Quick Start Guide & CMD Commands

### 1. Clone or Open Project Folder in CMD
Open Command Prompt (`cmd`) and navigate to your project directory:
```cmd
cd path\to\edge-ml-project
```

### 2. Train the Model & Generate `model.joblib`
Run the training script to generate the synthetic dataset and train the Random Forest model:
```cmd
python train_model.py
```

### 3. Build and Run the Edge ML Docker Container
Build the Docker image and run it locally mapping port `5001`:
```cmd
docker build -t motor-ml-module .
docker run -d -p 5001:5001 --name edge-ml-service motor-ml-module
```

### 4. Run the IoT Sensor Data Simulator
In a separate Command Prompt window, run the simulator to stream live telemetry and test real-time predictions:
```cmd
python simulate_sensor.py
```

---

## Pushing to GitHub via CMD
Run the following Git commands in your project folder to push the code to GitHub:

```cmd
git init
git add .
git commit -m "Initial commit: Real-Time ML Edge Application"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
git push -u origin main
```
