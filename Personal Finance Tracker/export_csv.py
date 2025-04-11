# export_csv.py

import pandas as pd
from reporting import get_dataframe

def export_to_csv(filename="transactions_export.csv"):
    df = get_dataframe()
    if df.empty:
        print("⚠️ No data to export.")
        return

    try:
        df.to_csv(filename, index=False)
        print(f"✅ Data exported to {filename}")
    except Exception as e:
        print(f"❌ Failed to export: {e}")
