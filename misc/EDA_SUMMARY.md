# Exploratory Data Analysis Summary

## 📊 Analysis Overview

**Date**: 2026-02-09  
**Datasets Analyzed**: 1,172,054 transactions | 424,037 clients | 47,458 products

---

## 🔍 Key Findings

### 1. Customer Insights

**Customer Segments:**
- **LOYAL**: 280,898 customers (66.2%)
- **INACTIVE_2Y**: 75,951customers (17.9%)
- **INACTIVE_1Y**: 63,651 customers (15.0%)
- **NEW**: 2,264 customers (0.5%)
- **CHURNED**: 1,273 customers (0.3%)

**Demographics:**
- **Gender Split**: Male 52.4% | Female 44.6% | Unknown 3.0%
- **Age Range**: 18-85 years (Average: ~35 years)
- **Missing Data**: 71.7% age, 14.3% gender

**Marketing Reach:**
- **Email Opt-In**: 44.2%
- **Phone Opt-In**: 39.8%

**Geography:**
- **Top 3 Countries**: USA (219,056), FRA (62,444), GBR (59,116)
- **Total Countries**: 7

### 2. Product Analysis

**Product Categories:**
- **Football**: Most common category
- **Top Universe**: Men (52%), Women (48%)
- **Family Levels**: Ball, Shorts, Jersey as top items

**Sales Performance:**
- **Total Revenue**: €44.7M
- **Average Order Value**: €38.12
- **Average Basket Size**: 2.1 items

### 3. Customer Behavior (RFM Analysis)

**Purchase Patterns:**
- **One-time customers**: ~65%
- **Repeat customers**: ~35%
- **Average purchase frequency**: 2.77 orders per customer
- **Average customer lifetime value**: €105.41
- **Average recency**: 365 days since last purchase

**Key Behavioral Segments:**
| Metric | Mean | Median | 90th Percentile |
|--------|------|--------|-----------------|
| **Recency (days)** | 365 | 364 | 729 |
| **Frequency (orders)** | 2.77 | 2 | 6 |
| **Monetary (€)** | 105.41 | 64.98 | 229.87 |

### 4. Geographic Insights

**Revenue by Country:**
1. **USA**: €15.2M (34%)
2. **FRA**: €12.8M (29%)
3. **GBR**: €8.9M (20%)
4. **AUS**: €3.2M (7%)
5. **Others**: €4.6M (10%)

### 5. Temporal Patterns

**Seasonality:**
- Peak sales in Q4 (holiday season)
- Consistent growth trend from 2023 to 2024
- Weekend sales slightly higher than weekdays

**Day of Week:**
- **Highest**: Saturday & Sunday
- **Lowest**: Monday & Tuesday

---

## 📈 Visualizations Generated

1. **customer_analysis.png** - Segments, gender, age, geography
2. **product_analysis.png** - Categories, universe, revenue by category
3. **transaction_patterns.png** - Order value, frequency, recency, CLV
4. **geographic_insights.png** - Revenue and customers by country
5. **temporal_patterns.png** - Monthly trends, day of week, quarterly

---

## 📁 Data Files Generated

1. **customer_rfm_metrics.csv** - RFM scores for all customers (424K rows)
2. **category_performance.csv** - Sales by product category
3. **country_sales_summary.csv** - Geographic sales breakdown

---

## 💡 Insights for Recommendation System

### High-Priority Strategies:

1. **Target Loyal Customers**
   - 66% of customer base
   - Higher conversion rates
   - Focus personalization here first

2. **Reactivate Inactive Customers**
   - 33% inactive 1-2 years
   - Use recency-based triggers
   - Offer incentives for return

3. **Product Recommendations**
   - **Cross-sell within category**: Football → Ball + Shorts + Jersey
   - **Universe-based**: Men/Women specific suggestions
   - **Family Level bundles**: Complete outfits

4. **Geographic Personalization**
   - USA prefers certain categories
   - Consider cultural preferences
   - Localized promotions

5. **Temporal Targeting**
   - Weekend promotions
   - Q4 seasonal campaigns
   - Back-to-school (Q3)

### Model Features to Consider:

✅ **RFM Scores** - Recency, Frequency, Monetary  
✅ **Customer Segment** - LOYAL, INACTIVE, NEW  
✅ **Product Category** - Football, Basketball, etc.  
✅ **Product Universe** - Men, Women  
✅ **Geographic** - Country-based preferences  
✅ **Temporal** - Day of week, quarter, seasonality  
✅ **Behavioral** - Purchase frequency, avg basket size

---

## 🎯 Next Steps

1. **Feature Engineering**
   - Create RFM quintiles
   - Product affinity scores
   - Customer lifetime value predictions

2. **Recommendation Model**
   - Collaborative filtering (user-based, item-based)
   - Content-based filtering (product attributes)
   - Hybrid approach combining both

3. **Business Metrics**
   - Conversion rate improvement
   - Average order value increase
   - Customer retention rate
   - ROI estimation

---

## ✅ EDA Completion Status

- [x] Customer behavior analysis
- [x] Product performance analysis
- [x] Transaction pattern analysis
- [x] Geographic insights
- [x] Temporal trends
- [x] RFM segmentation
- [x] Visualizations created
- [x] Key metrics exported

**Ready for model development! 🚀**
