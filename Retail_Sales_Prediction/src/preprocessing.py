# src/preprocessing.py

from data_loader import load_data
import pandas as pd

def preprocess_data():
    # Step 1: Load
    df = load_data()

    # Step 2: Drop missing CustomerID rows (optional based on your data)
    print("\nOriginal Data Shape:", df.shape)
    df = df.dropna(subset=['InvoiceNo', 'InvoiceDate', 'Quantity', 'UnitPrice'])
    print("Shape after dropping missing InvoiceNo/Date/Quantity/UnitPrice:", df.shape)

    # Step 3: Fix types
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
    df['UnitPrice'] = pd.to_numeric(df['UnitPrice'], errors='coerce')
    df['TotalSales'] = df['Quantity'] * df['UnitPrice']

    # Step 4: Drop Duplicates
    before = df.shape[0]
    df = df.drop_duplicates()
    after = df.shape[0]
    print(f"Dropped {before-after} duplicate rows")

    # Step 5: Handle Outliers (Simple Rule)
    df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]

    # Step 6: Final Shape
    print("\nFinal Cleaned Data Shape:", df.shape)

    return df

# If we run this script directly
if __name__ == "__main__":
    cleaned_df = preprocess_data()
