# main.py

from db import add_transaction, fetch_all_transactions
from reporting import (
    get_dataframe, get_summary,
    group_by_category, monthly_summary,
    generate_monthly_report,
    plot_expense_by_category, plot_monthly_trends, plot_expense_pie
)
from export_csv import export_to_csv
from datetime import datetime

def handle_add_transaction():

    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category (e.g. Groceries, Rent, Salary): ")
        ttype = input("Enter type (income/expense): ").lower()
        date_str = input("Enter date (YYYY-MM-DD): ")

        # Validate type
        if ttype not in ['income', 'expense']:
            print("❌ Type must be 'income' or 'expense'")
            return

        # Validate date
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print("❌ Invalid date format")
            return

        add_transaction(amount, category, ttype, date_str)

    except ValueError:
        print("❌ Invalid input. Please enter valid numbers and formats.")

def show_summary(df):
    if df.empty:
        print("⚠️ No data available.")
        return

    print("\n🔍 Summary:")
    print(get_summary(df))

    print("\n📂 Expenses by Category:")
    print(group_by_category(df))

    print("\n📅 Monthly Summary:")
    print(monthly_summary(df))

    generate_monthly_report(df)

def show_charts(df):
    if df.empty:
        print("⚠️ No data available.")
        return

    plot_expense_by_category(df)
    plot_monthly_trends(df)
    plot_expense_pie(df)

def menu():
    while True:
        print("\n📊 Personal Finance Tracker")
        print("=" * 30)
        print("1. Add Transaction")
        print("2. Show Summary & Report")
        print("3. Show Charts")
        print("4. Export to CSV")
        print("5. Exit")
        print("=" * 30)

        choice = input("Select an option (1–5): ")

        df = get_dataframe()

        if choice == '1':
            handle_add_transaction()
        elif choice == '2':
            show_summary(df)
        elif choice == '3':
            show_charts(df)
        elif choice == '4':
            export_to_csv("my_finance_backup.csv")
        elif choice == '5':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
