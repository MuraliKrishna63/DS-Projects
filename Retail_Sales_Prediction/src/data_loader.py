# src/data_loader.py

import pandas as pd

def load_data():
    file_path = "src/online_retail.csv"  # File directly inside src

    # Very important - using correct encoding
    try:
        df = pd.read_csv(file_path, encoding='ISO-8859-1')
    except UnicodeDecodeError:
        df = pd.read_csv(file_path, encoding='Windows-1252')

    print("Data Loaded Successfully! Showing Top 5 Rows:")
    print(df.head())

    return df
