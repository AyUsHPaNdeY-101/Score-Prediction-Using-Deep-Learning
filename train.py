import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

df = pd.read_csv("data/ipl_data.csv")

X = df[['runs', 'wickets', 'overs', 'runs_last_5', 'wickets_last_5']]
y = df['total']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

joblib.dump(scaler, "model/scaler.pkl")

model = Sequential([
    Dense(128, activation='relu', input_shape=(5,)),
    Dense(64, activation='relu'),
    Dense(1, activation='linear') 
])

model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])

print("Training model...")
model.fit(X_train, y_train, epochs=10, verbose=1)

loss, mae = model.evaluate(X_test, y_test)
print("loss", loss)
print("Mean Absolute Error", mae)

model.save("model/ipl_model.keras")
print("Model saved to model/ipl_model.keras")