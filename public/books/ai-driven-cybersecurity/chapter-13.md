# ✅ **Chapter 13: Build Your First ML Threat Detection Model**

### *A complete beginner-friendly project to detect cyber threats using Machine Learning*

---

# 📌 **Introduction**

You’ve learned how AI and ML power modern security systems.
Now it’s time to **build your first real, working ML model** for threat detection.

This chapter gives you:

* a **simple but powerful project**
* completely beginner-friendly
* uses real-world cybersecurity data
* does not require deep math
* runs on Google Colab
* takes 30–45 minutes to complete

By the end, you’ll create an ML model that can:
✔ detect malicious network traffic
✔ classify normal vs. attack behaviour
✔ be used for SOC automation
✔ serve as your first AI cybersecurity portfolio project

Let’s begin.

---

# 🎯 **1. What You Will Build**

You will build a **Network Intrusion Detection Model** using ML to detect:

* port scanning
* brute force attacks
* DDoS
* botnets
* malicious flows

We use a popular dataset:

### **CIDDS-001 or UNSW-NB15**

Both simulate real enterprise network traffic.

Your ML model will:

1. Load dataset
2. Extract features
3. Train a classification model
4. Predict malicious vs benign traffic
5. Evaluate accuracy

---

# 🧰 **2. Tools Needed (Free)**

Everything is 100% free and cloud-based.

### Use:

* **Google Colab** (recommended)
* **Python 3**
* **Scikit-Learn**
* **Pandas**
* **NumPy**
* **Matplotlib**

No installation needed.

---

# 📊 **3. Understanding the Dataset (Simple Explanation)**

### Each row = one network flow

Contains:

* source IP
* destination IP
* port
* protocol
* duration
* bytes sent
* packets
* flags
* labels (normal or attack)

ML learns from these patterns.

---

# ✨ **4. ML Workflow Overview**

Here’s the exact flow of your project:

```
Dataset
   ↓
Data Cleaning
   ↓
Feature Selection
   ↓
Train-Test Split
   ↓
Model Training (Random Forest)
   ↓
Evaluation
   ↓
Threat Predictions
```

This pipeline is universal in cybersecurity ML.

---

# 🧪 **5. Build the Model (Code Included)**

Copy + paste this into Google Colab.

---

## **STEP 1 — Install Libraries**

```python
!pip install pandas numpy scikit-learn matplotlib
```

---

## **STEP 2 — Import Libraries**

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import matplotlib.pyplot as plt
```

---

## **STEP 3 — Load the Dataset**

If using UNSW-NB15:

```python
from google.colab import files
uploaded = files.upload()
df = pd.read_csv('UNSW-NB15.csv')
```

If using CIDDS-001:

```python
df = pd.read_csv('cidds.csv')
```

---

## **STEP 4 — Basic Cleaning**

```python
df = df.dropna()
df = df.select_dtypes(include=[np.number])
```

This removes text columns and keeps numeric features only.

---

## **STEP 5 — Define Features & Labels**

```python
X = df.drop('label', axis=1)
y = df['label']
```

If your dataset uses “attack” instead:

```python
y = df['attack']
```

---

## **STEP 6 — Train-Test Split**

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42)
```

---

## **STEP 7 — Train Random Forest Model**

Random Forest is great for beginners.

```python
model = RandomForestClassifier(n_estimators=150)
model.fit(X_train, y_train)
```

---

## **STEP 8 — Model Predictions**

```python
y_pred = model.predict(X_test)
```

---

## **STEP 9 — Evaluate Model**

```python
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
```

If accuracy is >85%, your model is performing well.

---

# 🧠 **6. Understanding Your Model’s Output**

Your output will look like:

```
Accuracy: 0.91
Precision    Recall    F1-score
Benign        0.92       0.88
Malicious     0.90       0.93
```

### What this means:

* **Accuracy 91%** → Model works well
* **Precision** → How exact predictions are
* **Recall** → How many threats were correctly found
* **F1-score** → Balance between precision & recall

Security analysts focus on **recall**, because missing attacks is dangerous.

---

# 📊 **7. Visualizing Feature Importance**

Add this code:

```python
importances = model.feature_importances_
indices = np.argsort(importances)[-10:]

plt.figure(figsize=(10,5))
plt.title("Top 10 Important Features")
plt.barh(range(len(indices)), importances[indices], align='center')
plt.yticks(range(len(indices)), [X.columns[i] for i in indices])
plt.show()
```

This graph shows what features matter most.

Common important features:

* `duration`
* `bytes`
* `src_port`
* `dst_port`
* `protocol`
* `pkt_count`

Your ML model becomes explainable — important for cybersecurity jobs.

---

# 🛡️ **8. Deploy the Model (Optional)**

Your model can be deployed as:

* a **local script**
* a **SIEM integration**
* a **SOC alerting tool**
* a **cloud function**
* a **REST API**

Example Python API (Flask):

```python
from flask import Flask, request
import joblib

app = Flask(__name__)
model = joblib.load("model.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    prediction = model.predict([list(data.values())])
    return str(prediction[0])

app.run()
```

You now have your own AI threat detector.

---

# 📁 **9. Portfolio Ideas (For Students)**

Add these to your cybersecurity portfolio:

* GitHub repo of this project
* Kaggle notebook
* LinkedIn post documenting the process
* PDF report including evaluation metrics
* A video demo on YouTube or Instagram

This massively boosts your employability.

---

# 🧩 **10. Diagram: ML Threat Detection Pipeline**

```
 +-------------------+
 |    Raw Traffic    |
 +---------+---------+
           |
    Feature Extractor
           |
 +---------+---------+
 |  ML Model (RF)    |
 +---------+---------+
           |
    Threat Prediction
 (Benign | Malicious)
```

---

# 🎓 **11. Common ML Models Used in Threat Detection**

| Model         | Best For                      |
| ------------- | ----------------------------- |
| Random Forest | first models, structured data |
| XGBoost       | high accuracy models          |
| SVM           | small datasets                |
| LSTM          | sequence-based logs           |
| Autoencoder   | anomaly detection             |
| CNN           | malware byte analysis         |

Your first project uses Random Forest — perfect for beginners.

---

# 📌 **Key Takeaways**

* This project teaches the basics of ML in cybersecurity.
* You built your first AI threat classifier using real data.
* It works for network anomaly detection, SOC automation, and security analysis.
* You learned feature extraction, model training, evaluation, and visualization.
* This can be added to your cybersecurity portfolio immediately.

---
