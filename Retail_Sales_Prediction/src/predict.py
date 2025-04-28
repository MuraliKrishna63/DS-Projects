# src/predict.py

import pandas as pd
import joblib
import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

# 🛠 Importing load_data
from data_loader import load_data

# Load the saved model
model_path = os.path.join('models', 'random_forest_model.pkl')
model = joblib.load(model_path)

# Load the data using load_data()
df = load_data()

# 🛠 Fix: Convert InvoiceDate to datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Feature Engineering (Same as before)
df['DayOfWeek'] = df['InvoiceDate'].dt.dayofweek
df['Month'] = df['InvoiceDate'].dt.month
# 🔥 Important: Create TotalSales column
df['TotalSales'] = df['Quantity'] * df['UnitPrice']

# Select Features
features = ['Quantity', 'UnitPrice']
target = 'TotalSales'

# Take a small sample for testing
sample_df = df.sample(100, random_state=42)

X_sample = sample_df[features]
y_sample = sample_df[target]

# Make Predictions
y_pred = model.predict(X_sample)

# Evaluate
mae = mean_absolute_error(y_sample, y_pred)
mse = mean_squared_error(y_sample, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_sample, y_pred)

print(f"\n✅ Prediction Completed on Sample Data")
print(f"MAE: {mae:.2f}")
print(f"MSE: {mse:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"R² Score: {r2:.2f}")

# Plot Actual vs Predicted
plt.figure(figsize=(10,6))
sns.scatterplot(x=y_sample, y=y_pred, color='blue', edgecolor='k')
plt.xlabel('Actual Total Sales')
plt.ylabel('Predicted Total Sales')
plt.title('Actual vs Predicted Sales')
plt.plot([y_sample.min(), y_sample.max()], [y_sample.min(), y_sample.max()], 'r--')  # Diagonal line
plt.grid(True)
plt.show()
