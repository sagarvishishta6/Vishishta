"""
Comprehensive Data Analysis and Report
Analyzes the datasets and creates detailed markdown report
"""

import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime

# Paths
DATA_DIR = Path(r"c:\Users\sagar\Desktop\data_YourNextPurchase\data")
REPORT_PATH = Path(r"c:\Users\sagar\Desktop\data_YourNextPurchase\data_preparation_report.md")

print("Loading datasets...")

# Load datasets
transactions = pd.read_csv(DATA_DIR / "transactions.csv")
clients = pd.read_csv(DATA_DIR / "clients.csv")
products = pd.read_csv(DATA_DIR / "products.csv")
stocks = pd.read_csv(DATA_DIR / "stocks.csv")
stores = pd.read_csv(DATA_DIR / "stores.csv")

print("Generating report...")

# Create markdown report
report = []
report.append("# Data Preparation Report")
report.append(f"\nGenerated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
report.append("---\n")

# 1. Dataset Overview
report.append("## 1. Dataset Overview\n")
report.append("| Dataset | Rows | Columns |")
report.append("| --- | ---: | ---: |")
report.append(f"| Transactions | {len(transactions):,} | {len(transactions.columns)} |")
report.append(f"| Clients | {len(clients):,} | {len(clients.columns)} |")
report.append(f"| Products | {len(products):,} | {len(products.columns)} |")
report.append(f"| Stocks | {len(stocks):,} | {len(stocks.columns)} |")
report.append(f"| Stores | {len(stores):,} | {len(stores.columns)} |\n")

# 2. Column Details
report.append("## 2. Column Details\n")

report.append("### Transactions")
report.append(f"```\n{transactions.columns.tolist()}\n```")
report.append(f"\n**Data Types:**\n```\n{transactions.dtypes.to_string()}\n```\n")

report.append("### Clients")
report.append(f"```\n{clients.columns.tolist()}\n```")
report.append(f"\n**Data Types:**\n```\n{clients.dtypes.to_string()}\n```\n")

report.append("### Products")
report.append(f"```\n{products.columns.tolist()}\n```")
report.append(f"\n**Data Types:**\n```\n{products.dtypes.to_string()}\n```\n")

# 3. Missing Values
report.append("## 3. Missing Values Analysis\n")

report.append("### Transactions")
trans_missing = transactions.isnull().sum()
if trans_missing.any():
    for col, count in trans_missing[trans_missing > 0].items():
        pct = (count / len(transactions)) * 100
        report.append(f"- **{col}**: {count:,} ({pct:.2f}%)")
else:
    report.append("- ✓ No missing values")

report.append("\n### Clients")
client_missing = clients.isnull().sum()
if client_missing.any():
    for col, count in client_missing[client_missing > 0].items():
        pct = (count / len(clients)) * 100
        report.append(f"- **{col}**: {count:,} ({pct:.2f}%)")
else:
    report.append("- ✓ No missing values")

report.append("\n### Products")
prod_missing = products.isnull().sum()
if prod_missing.any():
    for col, count in prod_missing[prod_missing > 0].items():
        pct = (count / len(products)) * 100
        report.append(f"- **{col}**: {count:,} ({pct:.2f}%)")
else:
    report.append("- ✓ No missing values")

# 4. Key Statistics
report.append("\n## 4. Key Statistics\n")

report.append(f"- **Unique Clients**: {clients.iloc[:, 0].nunique():,}")
report.append(f"- **Unique Products**: {products.iloc[:, 0].nunique():,}")
report.append(f"- **Total Transactions**: {len(transactions):,}")
report.append(f"- **Unique Stores**: {len(stores):,}")

# Check for country column
country_cols = [c for c in stores.columns if 'country' in c.lower() or 'pais' in c.lower()]
if country_cols:
    report.append(f"- **Countries**: {stores[country_cols[0]].nunique()}")
    report.append(f"\n**Country Distribution:**")
    for country, count in stores[country_cols[0]].value_counts().head(10).items():
        report.append(f"  - {country}: {count}")

# 5. Sample Data
report.append("\n## 5. Sample Data\n")

report.append("### Transactions (first 5 rows)")
report.append("```")
report.append(transactions.head(5).to_string())
report.append("```\n")

report.append("### Clients (first 5 rows)")
report.append("```")
report.append(clients.head(5).to_string())
report.append("```\n")

report.append("### Products (first 5 rows)")
report.append("```")
report.append(products.head(5).to_string())
report.append("```\n")

# 6. Data Quality Issues
report.append("## 6. Data Quality Issues to Address\n")

issues = []

# Check for duplicates
trans_dupes = transactions.duplicated().sum()
if trans_dupes > 0:
    issues.append(f"- ⚠️ **{trans_dupes:,} duplicate transactions** found")

client_dupes = clients.duplicated(subset=[clients.columns[0]]).sum()
if client_dupes > 0:
    issues.append(f"- ⚠️ **{client_dupes:,} duplicate clients** found")

# Check for negative values
numeric_cols = transactions.select_dtypes(include=[np.number]).columns
for col in numeric_cols:
    if 'price' in col.lower() or 'amount' in col.lower() or 'quantity' in col.lower():
        neg_count = (transactions[col] < 0).sum() if transactions[col].dtype in [np.float64, np.int64] else 0
        if neg_count > 0:
            issues.append(f"- ⚠️ **{neg_count:,} negative values** in {col}")

if not issues:
    issues.append("- ✓ No major data quality issues detected")

report.extend(issues)

# 7. Recommendations
report.append("\n## 7. Next Steps\n")
report.append("1. **Standardize identifiers**: Ensure client_id, product_id, and country codes are consistent")
report.append("2. **Handle timestamps**: Convert date columns to proper datetime format")
report.append("3. **Remove invalid transactions**: Filter out cancelled, negative, or duplicate records")
report.append("4. **Feature engineering**: Create recency, frequency, monetary (RFM) features")
report.append("5. **EDA**: Analyze customer behavior, product popularity, and temporal patterns")

# Write report 
with open(REPORT_PATH, 'w', encoding='utf-8') as f:
    f.write('\n'.join(report))

print(f"✓ Report saved to: {REPORT_PATH}")
print(f"\n{len(report)} lines written")
