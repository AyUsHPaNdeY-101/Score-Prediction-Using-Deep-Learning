# 🏏 IPL Score Predictor Using Deep Learning

Welcome to the **IPL Score Predictor**! This project leverages the power of Deep Learning to predict the final innings score of an Indian Premier League (IPL) match based on the current match situation. Whether you're a cricket fanatic or a data science enthusiast, this project hits it out of the park! 🚀

## 🌟 What Does It Do?

Ever wondered what the final score will be while watching the first innings of a T20 match? This model takes in real-time match stats and predicts the final total. 

It uses a **Feedforward Neural Network** (built with TensorFlow & Keras) trained on historical IPL data to make intelligent estimations based on:
- 🏏 Current **Runs**
- 📉 Current **Wickets** fallen
- ⏱️ Current **Overs** bowled
- 🔥 **Runs** scored in the last 5 overs
- 🎯 **Wickets** fallen in the last 5 overs

## 📂 Project Structure

Here's how the locker room is organized:

- 📁 `data/` - Home pitch. Contains the dataset `ipl_data.csv` used for training the model.
- 📁 `model/` - The playbook. Stores the trained Keras deep learning model (`ipl_model.keras`) and the data scaler (`scaler.pkl`).
- 📁 `templates/` - The stadium. Contains the `index.html` template for our beautiful web interface.
- 📜 `app.py` - The umpire. A Flask web application that serves the frontend and makes live predictions using the trained model.
- ⚙️ `train.py` - The coach. The script responsible for data preprocessing, training the neural network, evaluating its performance, and saving the model.
- 📦 `requirements.txt` - The kit bag. Lists all necessary Python dependencies (`tensorflow`, `flask`, `scikit-learn`, `pandas`, etc.).

## 🚀 How to Run Locally

Ready to play? Follow these steps to get the project running on your local machine.

### 1. Install Dependencies
Make sure you have Python installed, then gear up by running:
```bash
pip install -r requirements.txt
```

### 2. Prepare the Data
Ensure your `ipl_data.csv` is securely placed inside the `data/` directory.

### 3. Train the Model (Optional)
If you want to train the deep learning model from scratch, run the training script. It will preprocess the data, train the model over 10 epochs, and save the artifacts in the `model/` directory:
```bash
python train.py
```

### 4. Start the Flask App
Fire up the web application to start predicting scores!
```bash
python app.py
```
*Note: Open `http://127.0.0.1:5000/` in your browser to access the interactive web interface.*

---
*Built with ❤️ for Cricket and Data!*
