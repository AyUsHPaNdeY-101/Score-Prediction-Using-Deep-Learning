<div align="center">

# 🏏 IPL Score Predictor Using Deep Learning 🏆

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg?style=for-the-badge&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-D00000.svg?style=for-the-badge&logo=Keras&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000.svg?style=for-the-badge&logo=Flask&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)

*Predicting the thrill of T20 cricket using the power of Neural Networks!*

[Explore the Code](#-project-structure) • [How to Run](#-how-to-run-locally) • [Tech Stack](#%EF%B8%8F-tech-stack)

</div>

---

## 🌟 What Does It Do?

Ever wondered what the final score will be while watching the first innings of a T20 match? This model takes in real-time match stats and predicts the final total with impressive accuracy!

It uses a **Feedforward Neural Network** trained on historical IPL data to make intelligent estimations based on:

| Match Metric | Description |
| :--- | :--- |
| 🏏 **Current Runs** | The total runs scored by the batting team so far. |
| 📉 **Current Wickets** | The number of wickets fallen. |
| ⏱️ **Current Overs** | The number of overs bowled. |
| 🔥 **Runs in Last 5 Overs** | Momentum indicator (runs scored recently). |
| 🎯 **Wickets in Last 5 Overs** | Pressure indicator (wickets fallen recently). |

---


## ⚙️ Tech Stack

- **Machine Learning**: TensorFlow, Keras, Scikit-Learn, Pandas, NumPy
- **Backend API**: Flask
- **Frontend UI**: HTML

---

## 📂 Project Structure

Here's how the locker room is organized:

```text
ipl_score_predictor/
│
├── 📁 data/                 # 🏏 Home pitch: Contains the training dataset (ipl_data.csv)
├── 📁 model/                # 🧠 The playbook: Stores trained model & scaler
├── 📁 templates/            # 🏟️ The stadium: Contains the frontend UI (index.html)
│
├── 📜 app.py                # 📢 The umpire: Flask app serving live predictions
├── ⚙️ train.py              # 🏋️ The coach: Data prep, training, and model evaluation
└── 📦 requirements.txt      # 🎒 The kit bag: Python dependencies
```

---

## 🚀 How to Run Locally

Ready to play? Follow these steps to get the project running on your local machine.

### 1️⃣ Install Dependencies
Make sure you have Python installed, then gear up by running:
```bash
pip install -r requirements.txt
```

### 2️⃣ Prepare the Data
Ensure your `ipl_data.csv` is securely placed inside the `data/` directory.

### 3️⃣ Train the Model (Optional)
If you want to train the deep learning model from scratch, run the training script. It will preprocess the data, train the model over 10 epochs, and save the artifacts in the `model/` directory:
```bash
python train.py
```

### 4️⃣ Start the Flask App
Fire up the web application to start predicting scores!
```bash
python app.py
```
> **Note**: Open `http://127.0.0.1:5000/` in your browser to access the interactive web interface.

---

