# reporting.py

import pandas as pd
from db import fetch_all_transactions

def get_dataframe():
    """Fetch transactions and convert them to a DataFrame"""
    transactions = fetch_all_transactions()
    if not transactions:
        print("⚠️ No data found.")
        return pd.DataFrame()

    df = pd.DataFrame(transactions)
    df['date'] = pd.to_datetime(df['date'])  # Ensure date column is datetime
    return df

def get_summary(df):
    """Return total income, total expenses, and balance"""
    income = df[df['type'] == 'income']['amount'].sum()
    expenses = df[df['type'] == 'expense']['amount'].sum()
    balance = income - expenses

    return {
        'Total Income': income,
        'Total Expenses': expenses,
        'Net Balance': balance
    }

def group_by_category(df):
    """Group expenses by category and return totals"""
    return df[df['type'] == 'expense'].groupby('category')['amount'].sum().sort_values(ascending=False)

def monthly_summary(df):
    """Monthly total income and expenses"""
    df['month'] = df['date'].dt.to_period('M')
    summary = df.groupby(['month', 'type'])['amount'].sum().unstack().fillna(0)
    summary['Net'] = summary.get('income', 0) - summary.get('expense', 0)
    return summary

import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")  # Optional: cleaner plots

def plot_expense_by_category(df):
    data = group_by_category(df).reset_index()
    plt.figure(figsize=(10, 5))
    sns.barplot(data=data, x="category", y="amount", palette="viridis")
    plt.title("Expenses by Category")
    plt.ylabel("Amount")
    plt.xlabel("Category")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_monthly_trends(df):
    monthly = monthly_summary(df)
    plt.figure(figsize=(10, 5))
    monthly[['income', 'expense']].plot(kind='line', marker='o')
    plt.title("Monthly Income vs Expenses")
    plt.ylabel("Amount")
    plt.xlabel("Month")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_expense_pie(df):
    data = group_by_category(df)
    plt.figure(figsize=(6, 6))
    data.plot(kind='pie', autopct='%1.1f%%')
    plt.title("Expense Distribution by Category")
    plt.ylabel("")  # Hide y-axis label
    plt.tight_layout()
    plt.show()


def generate_monthly_report(df):
    """Generate a clean, readable report for each month"""
    if df.empty:
        print("⚠️ No transactions to report.")
        return

    df['month'] = df['date'].dt.to_period('M')
    grouped = df.groupby(['month', 'type'])['amount'].sum().unstack().fillna(0)
    grouped['Net'] = grouped.get('income', 0) - grouped.get('expense', 0)

    print("\n📅 Monthly Finance Report")
    print("=" * 30)

    for index, row in grouped.iterrows():
        print(f"\n🗓 Month: {index}")
        print(f"   💰 Income   : {row.get('income', 0):.2f}")
        print(f"   💸 Expenses : {row.get('expense', 0):.2f}")
        print(f"   🧾 Net      : {row['Net']:.2f}")

        # Add a friendly comment
        if row['Net'] > 0:
            print("   ✅ Great job saving this month! 🎉")
        elif row['Net'] < 0:
            print("   ⚠️ Spent more than you earned! Let's improve. 💡")
        else:
            print("   📊 You broke even. Nice balance!")

    print("=" * 30)
