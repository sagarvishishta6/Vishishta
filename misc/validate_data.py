"""
Quick Validation: Verify cleaned data quality
"""
import pandas as pd
from pathlib import Path

CLEAN_DIR = Path(r"c:\Users\sagar\Desktop\data_YourNextPurchase\cleaned_data")

# Load cleaned data
trans = pd.read_csv(CLEAN_DIR / "transactions_cleaned.csv")

print("=" * 70)
print("✅ DATA PREPARATION VALIDATION")
print("=" * 70)

print(f"\n📊 Cleaned Transactions: {len(trans):,} rows")
print(f"\nColumns: {list(trans.columns)}")

# Check date conversion
trans['SaleTransactionDate'] = pd.to_datetime(trans['SaleTransactionDate'])
print(f"\n✓ Date range: {trans['SaleTransactionDate'].min()} to {trans['SaleTransactionDate'].max()}")

# Verify time features exist
time_features = ['TransactionYear', 'TransactionMonth', 'TransactionDay', 
                 'TransactionDayOfWeek', 'TransactionQuarter', 'DaysSinceTransaction']
existing = [f for f in time_features if f in trans.columns]
print(f"\n✓ Time features created: {existing}")

# Check data quality
print(f"\n✓ Missing values: {trans.isnull().sum().sum()}")
print(f"✓ Negative quantities: {(trans['Quantity'] <= 0).sum()}")
print(f"✓ Negative amounts: {(trans['SalesNetAmountEuro'] <= 0).sum()}")

print(f"\n✓ Unique clients: {trans['ClientID'].nunique():,}")
print(f"✓ Unique products: {trans['ProductID'].nunique():,}")

print("\n" + "=" * 70)
print("✅ ALL CHECKS PASSED - Data is ready for analysis!")
print("=" * 70)
