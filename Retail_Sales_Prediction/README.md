# Retail Sales Prediction Project

## Project Overview
This project focuses on predicting **retail sales** based on historical transaction data. Using machine learning models like **Linear Regression**, **Decision Tree**, and **Random Forest**, we forecast the `TotalSales` value.

The project is implemented **purely in Python scripts** (no Jupyter notebooks), with a clean structure and clear steps: **EDA**, **Modeling**, and **Prediction**.

---

## Project Structure
```
Retail_Sales_Prediction/
|├── src/
|   |├── data_loader.py
|   |├── eda.py
|   |├── modeling.py
|   └── predict.py
|├── online_retail.csv
|└── README.md
```

---

## How to Run

1. Install dependencies:
pip install -r requirements.txt

2. Run EDA:
py src/eda.py

3. Run Modeling:
py src/modeling.py

4. Run Predictions:
py src/predict.py

---

## Key Results

### Model Performance
| Model                   | MAE   | MSE    | RMSE  | R² Score |
|------------------------ |-------|--------|-------|----------|
| Linear Regression       | 10.70 | 2848.05| 53.37 | 0.58     |
| Decision Tree Regressor | 0.16  | 127.68 | 11.30 | 0.98     |
| Random Forest Regressor*| 0.14  | 72.24  | 8.50  | 0.99     |

### Prediction Results on Sample Data
| Metric | Score |
|--------|-------|
| MAE    | 0.24  |
| MSE    | 2.12  |
| RMSE   | 1.45  |
| R² Score | 1.00  |

### Visualization
- A graph showing predictions vs. actual sales was plotted.
- The red line (predictions) passes closely through the blue points (true values).

---

## Requirements
- Python 3.10+
- pandas
- scikit-learn
- matplotlib
- sqlalchemy (optional if connecting to SQL databases)

---

Author: P. Murali Krishna 
Project: Retail Sales Prediction


