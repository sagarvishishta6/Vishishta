"""
Data Quality Report Generator
Generates a comprehensive report on the cleaned datasets
"""

import pandas as pd
import numpy as np
from pathlib import Path

# Paths
DATA_DIR = Path(r"c:\Users\sagar\Desktop\data_YourNextPurchase\data")
CLEAN_DIR = Path(r"c:\Users\sagar\Desktop\data_YourNextPurchase\cleaned_data")

print("=" * 80)
print("DATA QUALITY REPORT")
print("=" * 80)

# Load cleaned datasets
if CLEAN_DIR.exists():
    transactions = pd.read_csv(CLEAN_DIR / "transactions_cleaned.csv")
    clients = pd.read_csv(CLEAN_DIR / "clients_cleaned.csv")
    products = pd.read_csv(CLEAN_DIR / "products_cleaned.csv")
    stocks = pd.read_csv(CLEAN_DIR / "stocks_cleaned.csv")
    stores = pd.read_csv(CLEAN_DIR / "stores_cleaned.csv")
else:
    # Load original if cleaned doesn't exist yet
    transactions = pd.read_csv(DATA_DIR / "transactions.csv")
    clients = pd.read_csv(DATA_DIR / "clients.csv")
    products = pd.read_csv(DATA_DIR / "products.csv")
    stocks = pd.read_csv(DATA_DIR / "stocks.csv")
    stores = pd.read_csv(DATA_DIR / "stores.csv")

# Generate report
print("\n1. DATASET DIMENSIONS")
print("-" * 80)
print(f"Transactions: {transactions.shape[0]:,} rows × {transactions.shape[1]} columns")
print(f"Clients:      {clients.shape[0]:,} rows × {clients.shape[1]} columns")
print(f"Products:     {products.shape[0]:,} rows × {products.shape[1]} columns")
print(f"Stocks:       {stocks.shape[0]:,} rows × {stocks.shape[1]} columns")
print(f"Stores:       {stores.shape[0]:,} rows × {stores.shape[1]} columns")

print("\n2. COLUMN OVERVIEW")
print("-" * 80)
print(f"\nTransactions columns: {list(transactions.columns)}")
print(f"\nClients columns: {list(clients.columns)}")
print(f"\nProducts columns: {list(products.columns)}")
print(f"\nStocks columns: {list(stocks.columns)}")
print(f"\nStores columns: {list(stores.columns)}")

print("\n3. DATA TYPES")
print("-" * 80)
print("\nTransactions:")
print(transactions.dtypes)

print("\nClients:")
print(clients.dtypes)

print("\nProducts:")
print(products.dtypes)

print("\n4. MISSING VALUES")
print("-" * 80)
print("\nTransactions:")
missing_trans = transactions.isnull().sum()
print(missing_trans[missing_trans > 0] if missing_trans.any() else "No missing values")

print("\nClients:")
missing_clients = clients.isnull().sum()
print(missing_clients[missing_clients > 0] if missing_clients.any() else "No missing values")

print("\nProducts:")
missing_products = products.isnull().sum()
print(missing_products[missing_products > 0] if missing_products.any() else "No missing values")

print("\n5. KEY STATISTICS")
print("-" * 80)
print(f"\nUnique clients: {clients.iloc[:, 0].nunique():,}")
print(f"Unique products: {products.iloc[:, 0].nunique():,}")
print(f"Unique stores: {stores.iloc[:, 0].nunique():,}")
print(f"Countries: {stores.iloc[:, 1].nunique() if len(stores.columns) > 1 else 'N/A'}")

# Date range for transactions
date_cols = [col for col in transactions.columns if 'date' in col.lower()]
if date_cols:
    print(f"\nTransaction date range:")
    for col in date_cols:
        try:
            dates = pd.to_datetime(transactions[col], errors='coerce')
            print(f"  {col}: {dates.min()} to {dates.max()}")
        except:
            pass

print("\n6. SAMPLE DATA")
print("-" * 80)
print("\nTransactions (first 3 rows):")
print(transactions.head(3).to_string())

print("\n\nClients (first 3 rows):")
print(clients.head(3).to_string())

print("\n\nProducts (first 3 rows):")
print(products.head(3).to_string())

print("\n" + "=" * 80)
print("REPORT COMPLETE")
print("=" * 80)
