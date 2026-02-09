"""
FINAL Data Preparation Script - Business Ready
================================================
Implements all required data cleaning steps for the hackathon
"""

import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime

# Paths
DATA_DIR = Path(r"c:\Users\sagar\Desktop\data_YourNextPurchase\data\raw")
OUTPUT_DIR = Path(r"c:\Users\sagar\Desktop\data_YourNextPurchase\data\processed")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

print("="*80)
print("FINAL DATA PREPARATION - THE NEXT PURCHASE")
print("="*80)

# ============================================================================
# STEP 1: LOAD DATASETS
# ============================================================================
print("\n[STEP 1] Loading datasets...")
transactions = pd.read_csv(DATA_DIR / "transactions.csv")
clients = pd.read_csv(DATA_DIR / "clients.csv")
products = pd.read_csv(DATA_DIR / "products.csv")
stocks = pd.read_csv(DATA_DIR / "stocks.csv")
stores = pd.read_csv(DATA_DIR / "stores.csv")

print(f"✓ Loaded {len(transactions):,} transactions")
print(f"✓ Loaded {len(clients):,} clients")
print(f"✓ Loaded {len(products):,} products")
print(f"✓ Loaded {len(stocks):,} stock records")
print(f"✓ Loaded {len(stores):,} stores")

# ============================================================================
# STEP 2: CHECK MISSING VALUES & INCONSISTENCIES
# ============================================================================
print("\n[STEP 2] Checking missing values & inconsistencies...")

print("\n--- Transactions ---")
print(f"Missing values:\n{transactions.isnull().sum()}")
print(f"\n✓ No missing values in transactions" if not transactions.isnull().any().any() else "⚠️ Missing values detected")

print("\n--- Clients ---")
client_missing = clients.isnull().sum()
print(f"Missing values:\n{client_missing[client_missing > 0]}")
print(f"Total rows with any missing: {clients.isnull().any(axis=1).sum():,}")

print("\n--- Products ---")
print(f"Missing values:\n{products.isnull().sum()}")
print(f"\n✓ No missing values in products" if not products.isnull().any().any() else "⚠️ Missing values detected")

# ============================================================================
# STEP 3: STANDARDIZE IDENTIFIERS
# ============================================================================
print("\n[STEP 3] Standardizing identifiers...")

# Keep original column names but ensure consistency
print(f"\n✓ ClientID: {transactions['ClientID'].nunique():,} unique values")
print(f"✓ ProductID: {transactions['ProductID'].nunique():,} unique values")
print(f"✓ StoreID: {transactions['StoreID'].nunique():,} unique values")

# Standardize country codes in stores (uppercase, trimmed)
stores['StoreCountry'] = stores['StoreCountry'].str.upper().str.strip()
print(f"\n✓ Standardized country codes: {stores['StoreCountry'].unique()}")

# Ensure client segments are standardized
clients['ClientSegment'] = clients['ClientSegment'].str.upper().str.strip()
print(f"✓ Client segments: {clients['ClientSegment'].unique()}")

# ============================================================================
# STEP 4: FILTER OUT INVALID TRANSACTIONS
# ============================================================================
print("\n[STEP 4] Filtering out invalid transactions...")

orig_count = len(transactions)

# Remove duplicates
transactions_dedup = transactions.drop_duplicates()
print(f"✓ Removed {orig_count - len(transactions_dedup):,} duplicate transactions")

# Remove transactions with invalid quantities (≤ 0)
transactions_clean = transactions_dedup[transactions_dedup['Quantity'] > 0]
print(f"✓ Removed {len(transactions_dedup) - len(transactions_clean):,} transactions with Quantity ≤ 0")

# Remove transactions with invalid amounts (≤ 0 or null)
transactions_clean = transactions_clean[
    (transactions_clean['SalesNetAmountEuro'] > 0) & 
    (transactions_clean['SalesNetAmountEuro'].notna())
]
print(f"✓ Removed invalid amount transactions")

# Remove transactions with missing IDs
transactions_clean = transactions_clean.dropna(subset=['ClientID', 'ProductID', 'StoreID'])
print(f"✓ Removed transactions with missing IDs")

print(f"\nTotal removed: {orig_count - len(transactions_clean):,} ({(orig_count - len(transactions_clean))/orig_count*100:.2f}%)")
print(f"Final transaction count: {len(transactions_clean):,}")

# ============================================================================
# STEP 5: ENSURE TIMESTAMPS ARE USABLE
# ============================================================================
print("\n[STEP 5] Processing timestamps...")

# Convert to datetime
transactions_clean['SaleTransactionDate'] = pd.to_datetime(
    transactions_clean['SaleTransactionDate'], 
    errors='coerce'
)

# Extract useful time features
transactions_clean['TransactionYear'] = transactions_clean['SaleTransactionDate'].dt.year
transactions_clean['TransactionMonth'] = transactions_clean['SaleTransactionDate'].dt.month
transactions_clean['TransactionDay'] = transactions_clean['SaleTransactionDate'].dt.day
transactions_clean['TransactionDayOfWeek'] = transactions_clean['SaleTransactionDate'].dt.dayofweek
transactions_clean['TransactionQuarter'] = transactions_clean['SaleTransactionDate'].dt.quarter

# Calculate recency (days since transaction relative to most recent date)
max_date = transactions_clean['SaleTransactionDate'].max()
transactions_clean['DaysSinceTransaction'] = (max_date - transactions_clean['SaleTransactionDate']).dt.days

print(f"✓ Converted dates to datetime")
print(f"✓ Date range: {transactions_clean['SaleTransactionDate'].min()} to {transactions_clean['SaleTransactionDate'].max()}")
print(f"✓ Created time features: Year, Month, Day, DayOfWeek, Quarter, DaysSinceTransaction")

# Remove any rows with invalid dates
transactions_clean = transactions_clean[transactions_clean['SaleTransactionDate'].notna()]
print(f"✓ Removed transactions with invalid dates")

# ============================================================================
# STEP 6: SAVE CLEANED DATASETS
# ============================================================================
print("\n[STEP 6] Saving cleaned datasets...")

# Save cleaned files
transactions_clean.to_csv(OUTPUT_DIR / "transactions_cleaned.csv", index=False)
clients.to_csv(OUTPUT_DIR / "clients_cleaned.csv", index=False)
products.to_csv(OUTPUT_DIR / "products_cleaned.csv", index=False)
stocks.to_csv(OUTPUT_DIR / "stocks_cleaned.csv", index=False)
stores.to_csv(OUTPUT_DIR / "stores_cleaned.csv", index=False)

print(f"\n✓ Saved to: {OUTPUT_DIR}")
print(f"  - transactions_cleaned.csv ({len(transactions_clean):,} rows)")
print(f"  - clients_cleaned.csv ({len(clients):,} rows)")
print(f"  - products_cleaned.csv ({len(products):,} rows)")
print(f"  - stocks_cleaned.csv ({len(stocks):,} rows)")
print(f"  - stores_cleaned.csv ({len(stores):,} rows)")

# ============================================================================
# SUMMARY REPORT
# ============================================================================
print("\n" + "="*80)
print("DATA CLEANING SUMMARY")
print("="*80)

print("\n📊 Dataset Statistics:")
print(f"  • Transactions: {len(transactions_clean):,} (removed {orig_count - len(transactions_clean):,})")
print(f"  • Unique Clients: {transactions_clean['ClientID'].nunique():,}")
print(f"  • Unique Products: {transactions_clean['ProductID'].nunique():,}")
print(f"  • Unique Stores: {transactions_clean['StoreID'].nunique():,}")
print(f"  • Date Range: {transactions_clean['TransactionYear'].min()}-{transactions_clean['TransactionYear'].max()}")
print(f"  • Countries: {len(stores['StoreCountry'].unique())}")

print("\n✅ Data Quality:")
print(f"  • Missing values in transactions: {transactions_clean.isnull().sum().sum()}")
print(f"  • Missing Client Gender: {clients['ClientGender'].isnull().sum():,} ({clients['ClientGender'].isnull().sum()/len(clients)*100:.1f}%)")
print(f"  • Missing Client Age: {clients['Age'].isnull().sum():,} ({clients['Age'].isnull().sum()/len(clients)*100:.1f}%)")

print("\n🎯 Data is now BUSINESS-READY for:")
print("  1. Exploratory Data Analysis (EDA)")
print("  2. Feature Engineering (RFM, etc.)")
print("  3. Recommendation Model Building")
print("  4. Business Insights Generation")

print("\n" + "="*80)
print("✅ DATA PREPARATION COMPLETE!")
print("="*80)
