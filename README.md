# Student Mark Predictor

A simple **Machine Learning + Flask** web application that predicts student marks based on study hours (and optional additional inputs). This project is fully containerized using **Docker** and supports deployment using **docker-compose**.

---

## 🚀 Features

* Predict student marks using ML models (single & multiple feature models).
* Flask-based web UI.
* Pre-trained `.pkl` models included.
* CSV datasets for training and testing.
* Integrated Dockerfile and docker-compose setup.
* Automatic container startup via `entrypoint.sh`.

---

## 📂 Project Structure

```
├── app.py
├── docker-compose.yml
├── Dockerfile
├── entrypoint.sh
├── instance/
│   └── database.db
├── multiple_student_mark_prediction.pkl
├── student_mark_prediction.pkl
├── requirements.txt
├── static/
│   ├── css/
│   └── script.js
├── templates/
│   └── index.html
├── *.csv files (datasets)
├── *.ipynb files (model-building notebooks)
└── README.md
```

---

## 🧠 Model Details

Two ML models are included:

* `student_mark_prediction.pkl` – Uses **Study Hours**.
* `multiple_student_mark_prediction.pkl` – Uses **two input features**.

Models are trained in the provided Jupyter notebooks.

---

## 🖥️ Running the Project Locally

### 1️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 2️⃣ Run the Flask App

```
python app.py
```

App will run by default on:

```
http://127.0.0.1:5000
```

---

# 🐳 Docker Setup

## **Dockerfile**

```dockerfile
FROM python:3.10-slim

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

RUN chmod +x entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
```

---

## **docker-compose.yml**

```yaml
version: '3.8'
services:
  mark-predictor:
    build: .
    container_name: mark-predictor
    ports:
      - "5000:5000"
    volumes:
      - .:/app
    restart: always
```

---

## ▶️ Run Using Docker

### **1️⃣ Build the image**

```
docker build -t student-mark-predictor:1.0 .
```

### **2️⃣ Run container**

```
docker run -p 5000:5000 student-mark-predictor:1.0
```

---

## ▶️ Run Using Docker Compose

```
docker-compose up --build
```

App will be available at:

```
http://localhost:5000
```

---

## 📸 Screenshots

Add screenshots like:


![UI Screenshot](https://github.com/akshatraj26/Student-Mark-Prediction/blob/main/Screenshot%20(405).png)


![Prediction Output](https://github.com/akshatraj26/Student-Mark-Prediction/blob/main/Screenshot%20(407).png)

---

## ✨ Credits

Developed by **Akshat Raj**.

If you like this project, don't forget to ⭐ the repository!
