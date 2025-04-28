# src/modeling.py

from preprocessing import preprocess_data
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np
import joblib
import os

# Step 1: Load Clean Data
df = preprocess_data()

# Step 2: Feature Selection
X = df[['Quantity', 'UnitPrice']]  # features
y = df['TotalSales']               # target

# Step 3: Train Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Define Models
models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree Regressor": DecisionTreeRegressor(random_state=42),
    "Random Forest Regressor": RandomForestRegressor(random_state=42)
}

# Step 5: Train and Evaluate
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)

    print(f"\n{name}")
    print(f"MAE: {mae:.2f}")
    print(f"MSE: {mse:.2f}")
    print(f"RMSE: {rmse:.2f}")
    print(f"R² Score: {r2:.2f}")


# Save the Random Forest model
model_save_path = os.path.join('models', 'random_forest_model.pkl')
#joblib.dump(object, filepath)  #saves a Python object to a file.
joblib.dump(models['Random Forest Regressor'], model_save_path)

print(f"\n✅ Model saved successfully at: {model_save_path}")
