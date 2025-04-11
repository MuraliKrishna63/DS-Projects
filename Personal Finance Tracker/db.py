# db.py

import mysql.connector
from mysql.connector import Error
from config import DB_CONFIG

def create_connection():
    """Establish and return a database connection"""
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def add_transaction(amount, category, trans_type, date):
    """Insert a new income or expense transaction into the database"""
    conn = create_connection()
    if conn is None:
        return

    try:
        cursor = conn.cursor()
        query = """
            INSERT INTO transactions (amount, category, type, date)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (amount, category, trans_type, date))
        conn.commit()
        print("✅ Transaction added successfully.")
    except Error as e:
        print(f"❌ Failed to add transaction: {e}")
    finally:
        conn.close()

def fetch_all_transactions():
    """Retrieve all transactions from the database"""
    conn = create_connection()
    if conn is None:
        return []

    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM transactions")
        results = cursor.fetchall()
        return results
    except Error as e:
        print(f"❌ Error fetching transactions: {e}")
        return []
    finally:
        conn.close()
