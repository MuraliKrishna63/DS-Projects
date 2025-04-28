# src/eda.py

from data_loader import load_data
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
# Step 1: Load Data
df = load_data()

# Step 2: Quick EDA
print("\nColumns and Types:")
print(df.dtypes)

print("\nChecking for Nulls:")
print(df.isnull().sum())

# Step 3: Create TotalSales Column
df['TotalSales'] = df['Quantity'] * df['UnitPrice']

# Step 4: Plotting

# 4a: Daily Sales
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
daily_sales = df.groupby(df['InvoiceDate'].dt.date)['TotalSales'].sum()

plt.figure(figsize=(12, 6))
daily_sales.plot()
plt.title('Daily Total Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.grid(True)
plt.tight_layout()
plt.show()

# 4b: Top 10 Countries by Sales
top_countries = df.groupby('Country')['TotalSales'].sum().sort_values(ascending=False)[:10]

plt.figure(figsize=(10,5))
sns.barplot(x=top_countries.values, y=top_countries.index)
plt.title('Top 10 Countries by Sales')
plt.xlabel('Sales')
plt.ylabel('Country')
plt.tight_layout()
plt.show()
