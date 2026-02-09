"""
Exploratory Data Analysis (EDA) - The Next Purchase
====================================================
Comprehensive analysis of customer behavior, product trends, and patterns
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# Paths
CLEAN_DIR = Path(r"c:\Users\sagar\Desktop\data_YourNextPurchase\data\processed")
OUTPUT_DIR = Path(r"c:\Users\sagar\Desktop\data_YourNextPurchase\marketing\eda_outputs")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

print("="*80)
print("EXPLORATORY DATA ANALYSIS - THE NEXT PURCHASE")
print("="*80)

# ============================================================================
# LOAD CLEANED DATA
# ============================================================================
print("\n[1/7] Loading cleaned datasets...")

transactions = pd.read_csv(CLEAN_DIR / "transactions_cleaned.csv")
clients = pd.read_csv(CLEAN_DIR / "clients_cleaned.csv")
products = pd.read_csv(CLEAN_DIR / "products_cleaned.csv")
stocks = pd.read_csv(CLEAN_DIR / "stocks_cleaned.csv")
stores = pd.read_csv(CLEAN_DIR / "stores_cleaned.csv")

# Convert dates
transactions['SaleTransactionDate'] = pd.to_datetime(transactions['SaleTransactionDate'])

print(f"✓ Loaded {len(transactions):,} transactions")
print(f"✓ Loaded {len(clients):,} clients")
print(f"✓ Loaded {len(products):,} products")

# ============================================================================
# CUSTOMER ANALYSIS
# ============================================================================
print("\n[2/7] Analyzing customer behavior...")

# Customer segments
segment_dist = clients['ClientSegment'].value_counts()
print("\n--- Customer Segments ---")
print(segment_dist)
print(f"\nTotal segments: {len(segment_dist)}")

# Gender distribution
gender_dist = clients['ClientGender'].value_counts()
print("\n--- Gender Distribution ---")
print(gender_dist)

# Age distribution (non-null)
age_stats = clients['Age'].describe()
print("\n--- Age Statistics ---")
print(age_stats)

# Country distribution
country_dist = clients['ClientCountry'].value_counts()
print("\n--- Top 10 Countries (Clients) ---")
print(country_dist.head(10))

# Marketing opt-in rates
email_opt_in = clients['ClientOptINEmail'].mean() * 100
phone_opt_in = clients['ClientOptINPhone'].mean() * 100
print(f"\n--- Marketing Opt-In Rates ---")
print(f"Email: {email_opt_in:.1f}%")
print(f"Phone: {phone_opt_in:.1f}%")

# Create customer segment visualization
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Customer Analysis', fontsize=16, fontweight='bold')

# Segment distribution
segment_dist.plot(kind='bar', ax=axes[0, 0], color='skyblue')
axes[0, 0].set_title('Customer Segments')
axes[0, 0].set_xlabel('Segment')
axes[0, 0].set_ylabel('Count')
axes[0, 0].tick_params(axis='x', rotation=45)

# Gender distribution
gender_dist.plot(kind='pie', ax=axes[0, 1], autopct='%1.1f%%', startangle=90)
axes[0, 1].set_title('Gender Distribution')
axes[0, 1].set_ylabel('')

# Age distribution
clients['Age'].dropna().hist(bins=30, ax=axes[1, 0], color='lightcoral', edgecolor='black')
axes[1, 0].set_title('Age Distribution')
axes[1, 0].set_xlabel('Age')
axes[1, 0].set_ylabel('Frequency')

# Top countries
country_dist.head(10).plot(kind='barh', ax=axes[1, 1], color='lightgreen')
axes[1, 1].set_title('Top 10 Countries')
axes[1, 1].set_xlabel('Number of Clients')

plt.tight_layout()
plt.savefig(OUTPUT_DIR / 'customer_analysis.png', dpi=300, bbox_inches='tight')
print(f"\n✓ Saved: customer_analysis.png")
plt.close()

# ============================================================================
# PRODUCT ANALYSIS
# ============================================================================
print("\n[3/7] Analyzing products...")

# Category distribution
category_dist = products['Category'].value_counts()
print("\n--- Product Categories ---")
print(category_dist.head(10))

# Universe distribution
universe_dist = products['Universe'].value_counts()
print("\n--- Product Universe ---")
print(universe_dist)

# Family levels
family1_dist = products['FamilyLevel1'].value_counts()
print("\n--- Top 10 FamilyLevel1 ---")
print(family1_dist.head(10))

# Merge transactions with products to analyze sales
trans_products = transactions.merge(products, on='ProductID', how='left')

# Most sold categories
category_sales = trans_products.groupby('Category').agg({
    'Quantity': 'sum',
    'SalesNetAmountEuro': 'sum',
    'ProductID': 'count'
}).rename(columns={'ProductID': 'Transactions'})
category_sales = category_sales.sort_values('SalesNetAmountEuro', ascending=False)

print("\n--- Top 10 Categories by Revenue ---")
print(category_sales.head(10))

# Product visualization
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Product Analysis', fontsize=16, fontweight='bold')

# Category distribution
category_dist.head(10).plot(kind='barh', ax=axes[0, 0], color='coral')
axes[0, 0].set_title('Top 10 Product Categories')
axes[0, 0].set_xlabel('Count')

# Universe distribution
universe_dist.plot(kind='pie', ax=axes[0, 1], autopct='%1.1f%%', startangle=90)
axes[0, 1].set_title('Product Universe Distribution')
axes[0, 1].set_ylabel('')

# Top categories by revenue
category_sales['SalesNetAmountEuro'].head(10).plot(kind='bar', ax=axes[1, 0], color='gold')
axes[1, 0].set_title('Top 10 Categories by Revenue')
axes[1, 0].set_xlabel('Category')
axes[1, 0].set_ylabel('Revenue (€)')
axes[1, 0].tick_params(axis='x', rotation=45)

# Family level 1 distribution
family1_dist.head(10).plot(kind='barh', ax=axes[1, 1], color='lightblue')
axes[1, 1].set_title('Top 10 FamilyLevel1')
axes[1, 1].set_xlabel('Count')

plt.tight_layout()
plt.savefig(OUTPUT_DIR / 'product_analysis.png', dpi=300, bbox_inches='tight')
print(f"✓ Saved: product_analysis.png")
plt.close()

# ============================================================================
# TRANSACTION PATTERNS
# ============================================================================
print("\n[4/7] Analyzing transaction patterns...")

# Overall statistics
total_revenue = transactions['SalesNetAmountEuro'].sum()
total_quantity = transactions['Quantity'].sum()
avg_order_value = transactions['SalesNetAmountEuro'].mean()
avg_basket_size = transactions['Quantity'].mean()

print(f"\n--- Transaction Statistics ---")
print(f"Total Revenue: €{total_revenue:,.2f}")
print(f"Total Quantity Sold: {total_quantity:,}")
print(f"Average Order Value: €{avg_order_value:.2f}")
print(f"Average Basket Size: {avg_basket_size:.2f} items")

# Customer purchase frequency (RFM analysis)
customer_metrics = transactions.groupby('ClientID').agg({
    'SaleTransactionDate': ['min', 'max', 'count'],
    'SalesNetAmountEuro': 'sum',
    'Quantity': 'sum'
}).reset_index()

customer_metrics.columns = ['ClientID', 'FirstPurchase', 'LastPurchase', 'Frequency', 'MonetaryValue', 'TotalQuantity']

# Calculate recency (days since last purchase)
max_date = transactions['SaleTransactionDate'].max()
customer_metrics['Recency'] = (max_date - customer_metrics['LastPurchase']).dt.days

print(f"\n--- Customer Metrics (RFM) ---")
print(customer_metrics[['Recency', 'Frequency', 'MonetaryValue']].describe())

# One-time vs repeat customers
one_time_customers = (customer_metrics['Frequency'] == 1).sum()
repeat_customers = (customer_metrics['Frequency'] > 1).sum()
print(f"\nOne-time customers: {one_time_customers:,} ({one_time_customers/len(customer_metrics)*100:.1f}%)")
print(f"Repeat customers: {repeat_customers:,} ({repeat_customers/len(customer_metrics)*100:.1f}%)")

# Transaction patterns visualization
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Transaction Patterns', fontsize=16, fontweight='bold')

# Order value distribution
transactions['SalesNetAmountEuro'].hist(bins=50, ax=axes[0, 0], color='steelblue', edgecolor='black')
axes[0, 0].set_title('Order Value Distribution')
axes[0, 0].set_xlabel('Order Value (€)')
axes[0, 0].set_ylabel('Frequency')
axes[0, 0].set_xlim(0, transactions['SalesNetAmountEuro'].quantile(0.95))

# Purchase frequency distribution
customer_metrics['Frequency'].hist(bins=50, ax=axes[0, 1], color='orange', edgecolor='black')
axes[0, 1].set_title('Customer Purchase Frequency')
axes[0, 1].set_xlabel('Number of Purchases')
axes[0, 1].set_ylabel('Number of Customers')
axes[0, 1].set_xlim(0, customer_metrics['Frequency'].quantile(0.95))

# Recency distribution
customer_metrics['Recency'].hist(bins=50, ax=axes[1, 0], color='green', edgecolor='black')
axes[1, 0].set_title('Customer Recency (Days Since Last Purchase)')
axes[1, 0].set_xlabel('Days')
axes[1, 0].set_ylabel('Number of Customers')

# Monetary value distribution
customer_metrics['MonetaryValue'].hist(bins=50, ax=axes[1, 1], color='purple', edgecolor='black')
axes[1, 1].set_title('Customer Lifetime Value Distribution')
axes[1, 1].set_xlabel('Total Spent (€)')
axes[1, 1].set_ylabel('Number of Customers')
axes[1, 1].set_xlim(0, customer_metrics['MonetaryValue'].quantile(0.95))

plt.tight_layout()
plt.savefig(OUTPUT_DIR / 'transaction_patterns.png', dpi=300, bbox_inches='tight')
print(f"✓ Saved: transaction_patterns.png")
plt.close()

# ============================================================================
# GEOGRAPHIC INSIGHTS
# ============================================================================
print("\n[5/7] Analyzing geographic patterns...")

# Merge with stores to get country info
trans_stores = transactions.merge(stores, on='StoreID', how='left')

# Sales by country
country_sales = trans_stores.groupby('StoreCountry').agg({
    'SalesNetAmountEuro': 'sum',
    'Quantity': 'sum',
    'ClientID': 'nunique'
}).rename(columns={'ClientID': 'UniqueCustomers'})
country_sales = country_sales.sort_values('SalesNetAmountEuro', ascending=False)

print("\n--- Sales by Country ---")
print(country_sales)

# Geographic visualization
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
fig.suptitle('Geographic Insights', fontsize=16, fontweight='bold')

# Revenue by country
country_sales['SalesNetAmountEuro'].plot(kind='bar', ax=axes[0], color='teal')
axes[0].set_title('Revenue by Country')
axes[0].set_xlabel('Country')
axes[0].set_ylabel('Revenue (€)')
axes[0].tick_params(axis='x', rotation=45)

# Customers by country
country_sales['UniqueCustomers'].plot(kind='bar', ax=axes[1], color='salmon')
axes[1].set_title('Unique Customers by Country')
axes[1].set_xlabel('Country')
axes[1].set_ylabel('Number of Customers')
axes[1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig(OUTPUT_DIR / 'geographic_insights.png', dpi=300, bbox_inches='tight')
print(f"✓ Saved: geographic_insights.png")
plt.close()

# ============================================================================
# TEMPORAL PATTERNS
# ============================================================================
print("\n[6/7] Analyzing temporal patterns...")

# Sales over time
monthly_sales = transactions.groupby([transactions['SaleTransactionDate'].dt.to_period('M')]).agg({
    'SalesNetAmountEuro': 'sum',
    'Quantity': 'sum',
    'ClientID': 'count'
}).rename(columns={'ClientID': 'Transactions'})

print("\n--- Monthly Sales Trend ---")
print(monthly_sales.tail(10))

# Day of week patterns
dow_sales = transactions.groupby('TransactionDayOfWeek').agg({
    'SalesNetAmountEuro': 'mean',
    'Quantity': 'sum'
})
dow_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
dow_sales.index = [dow_names[i] for i in dow_sales.index]

print("\n--- Sales by Day of Week ---")
print(dow_sales)

# Temporal visualization
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Temporal Patterns', fontsize=16, fontweight='bold')

# Monthly revenue trend
monthly_sales['SalesNetAmountEuro'].plot(kind='line', ax=axes[0, 0], color='blue', marker='o')
axes[0, 0].set_title('Monthly Revenue Trend')
axes[0, 0].set_xlabel('Month')
axes[0, 0].set_ylabel('Revenue (€)')
axes[0, 0].grid(True, alpha=0.3)

# Monthly transactions trend
monthly_sales['Transactions'].plot(kind='line', ax=axes[0, 1], color='red', marker='s')
axes[0, 1].set_title('Monthly Transaction Volume')
axes[0, 1].set_xlabel('Month')
axes[0, 1].set_ylabel('Number of Transactions')
axes[0, 1].grid(True, alpha=0.3)

# Day of week revenue
dow_sales['SalesNetAmountEuro'].plot(kind='bar', ax=axes[1, 0], color='green')
axes[1, 0].set_title('Average Order Value by Day of Week')
axes[1, 0].set_xlabel('Day of Week')
axes[1, 0].set_ylabel('Average Order Value (€)')
axes[1, 0].tick_params(axis='x', rotation=45)

# Quarterly sales
quarterly_sales = transactions.groupby('TransactionQuarter')['SalesNetAmountEuro'].sum()
quarterly_sales.plot(kind='bar', ax=axes[1, 1], color='orange')
axes[1, 1].set_title('Revenue by Quarter')
axes[1, 1].set_xlabel('Quarter')
axes[1, 1].set_ylabel('Revenue (€)')

plt.tight_layout()
plt.savefig(OUTPUT_DIR / 'temporal_patterns.png', dpi=300, bbox_inches='tight')
print(f"✓ Saved: temporal_patterns.png")
plt.close()

# ============================================================================
# SAVE KEY METRICS
# ============================================================================
print("\n[7/7] Saving summary metrics and RFM data...")

# Save customer RFM metrics
customer_metrics.to_csv(OUTPUT_DIR / 'customer_rfm_metrics.csv', index=False)
print(f"✓ Saved: customer_rfm_metrics.csv")

# Save category performance
category_sales.to_csv(OUTPUT_DIR / 'category_performance.csv')
print(f"✓ Saved: category_performance.csv")

# Save geographic summary
country_sales.to_csv(OUTPUT_DIR / 'country_sales_summary.csv')
print(f"✓ Saved: country_sales_summary.csv")

# ============================================================================
# GENERATE EDA SUMMARY REPORT
# ============================================================================
print("\n" + "="*80)
print("EDA SUMMARY")
print("="*80)

print("\n📊 KEY FINDINGS:")
print(f"\n1. CUSTOMER BASE:")
print(f"   • Total customers: {len(clients):,}")
print(f"   • Most common segment: {segment_dist.index[0]} ({segment_dist.iloc[0]:,} customers)")
print(f"   • Email opt-in rate: {email_opt_in:.1f}%")
print(f"   • Repeat customer rate: {repeat_customers/len(customer_metrics)*100:.1f}%")

print(f"\n2. REVENUE & SALES:")
print(f"   • Total revenue: €{total_revenue:,.2f}")
print(f"   • Average order value: €{avg_order_value:.2f}")
print(f"   • Top category by revenue: {category_sales.index[0]}")
print(f"   • Top country by revenue: {country_sales.index[0]}")

print(f"\n3. PRODUCT INSIGHTS:")
print(f"   • Total products: {len(products):,}")
print(f"   • Most popular category: {category_dist.index[0]} ({category_dist.iloc[0]:,} products)")
print(f"   • Product universe: {', '.join(universe_dist.index.tolist())}")

print(f"\n4. CUSTOMER BEHAVIOR:")
print(f"   • Avg purchase frequency: {customer_metrics['Frequency'].mean():.2f} orders")
print(f"   • Avg customer lifetime value: €{customer_metrics['MonetaryValue'].mean():.2f}")
print(f"   • Avg recency: {customer_metrics['Recency'].mean():.1f} days")

print("\n📁 OUTPUT FILES:")
print(f"   • customer_analysis.png")
print(f"   • product_analysis.png")
print(f"   • transaction_patterns.png")
print(f"   • geographic_insights.png")
print(f"   • temporal_patterns.png")
print(f"   • customer_rfm_metrics.csv")
print(f"   • category_performance.csv")
print(f"   • country_sales_summary.csv")

print("\n🎯 RECOMMENDATIONS FOR MODEL:")
print("   1. Focus on repeat customers (higher conversion)")
print("   2. Leverage RFM metrics for customer segmentation")
print("   3. Use category and universe for content-based filtering")
print("   4. Consider temporal patterns for seasonal recommendations")
print("   5. Personalize by geography and customer segment")

print("\n" + "="*80)
print("✅ EXPLORATORY DATA ANALYSIS COMPLETE!")
print("="*80)
print(f"\nAll outputs saved to: {OUTPUT_DIR}")
