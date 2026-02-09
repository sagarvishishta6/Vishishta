# Data Preparation Report

Generated: 2026-02-09 10:58:23

---

## 1. Dataset Overview

| Dataset | Rows | Columns |
| --- | ---: | ---: |
| Transactions | 1,177,175 | 6 |
| Clients | 424,037 | 7 |
| Products | 47,458 | 5 |
| Stocks | 16,024 | 3 |
| Stores | 606 | 2 |

## 2. Column Details

### Transactions
```
['ClientID', 'ProductID', 'SaleTransactionDate', 'StoreID', 'Quantity', 'SalesNetAmountEuro']
```

**Data Types:**
```
ClientID                 int64
ProductID                int64
SaleTransactionDate        str
StoreID                  int64
Quantity                 int64
SalesNetAmountEuro     float64
```

### Clients
```
['ClientID', 'ClientSegment', 'ClientCountry', 'ClientOptINEmail', 'ClientOptINPhone', 'ClientGender', 'Age']
```

**Data Types:**
```
ClientID              int64
ClientSegment           str
ClientCountry           str
ClientOptINEmail      int64
ClientOptINPhone      int64
ClientGender            str
Age                 float64
```

### Products
```
['ProductID', 'Category', 'FamilyLevel1', 'FamilyLevel2', 'Universe']
```

**Data Types:**
```
ProductID       int64
Category          str
FamilyLevel1      str
FamilyLevel2      str
Universe          str
```

## 3. Missing Values Analysis

### Transactions
- ✓ No missing values

### Clients
- **ClientGender**: 60,795 (14.34%)
- **Age**: 304,075 (71.71%)

### Products
- ✓ No missing values

## 4. Key Statistics

- **Unique Clients**: 424,037
- **Unique Products**: 47,458
- **Total Transactions**: 1,177,175
- **Unique Stores**: 606
- **Countries**: 7

**Country Distribution:**
  - USA: 212
  - FRA: 185
  - GBR: 75
  - AUS: 52
  - ARE: 33
  - DEU: 30
  - BRA: 19

## 5. Sample Data

### Transactions (first 5 rows)
```
              ClientID            ProductID        SaleTransactionDate              StoreID  Quantity  SalesNetAmountEuro
0  8119209481417068505  3532473209579560668  2023-06-06 00:00:00+00:00  4821951108133690356         4               56.97
1  2497726585282787281  5103640511191568912  2023-09-20 00:00:00+00:00  1450109522794525790         1                5.99
2  7673687066317773168  4923931302917549451  2023-12-16 00:00:00+00:00  1821464542701843363         2               16.99
3  1873234305263900608  8502620308847538595  2023-01-31 00:00:00+00:00  2686511472610728845         4              140.97
4  3913817537779196185  8573693021421318503  2024-01-23 00:00:00+00:00  3600233866627167751         1               10.99
```

### Clients (first 5 rows)
```
              ClientID ClientSegment ClientCountry  ClientOptINEmail  ClientOptINPhone ClientGender  Age
0  4508698145640552159         LOYAL           USA                 1                 1            M  NaN
1  2022746661324934183   INACTIVE_1Y           USA                 0                 1            F  NaN
2  5794452591674300222         LOYAL           USA                 1                 1            F  NaN
3   678556389231830160         LOYAL           USA                 1                 1            M  NaN
4   877301557964624234         LOYAL           USA                 1                 1            F  NaN
```

### Products (first 5 rows)
```
             ProductID  Category FamilyLevel1  FamilyLevel2 Universe
0    43220326960179274  Football         Ball  Nike Ordem V    Women
1   622915065731236396  Football         Ball  Nike Ordem V      Men
2  2020543468978812774  Football       Shorts  Nike Dri-FIT    Women
3   600002891277549143  Football       Shorts  Nike Dri-FIT    Women
4  6150916997899913693  Football       Shorts  Nike Dri-FIT      Men
```

## 6. Data Quality Issues to Address

- ⚠️ **5,121 duplicate transactions** found

## 7. Next Steps

1. **Standardize identifiers**: Ensure client_id, product_id, and country codes are consistent
2. **Handle timestamps**: Convert date columns to proper datetime format
3. **Remove invalid transactions**: Filter out cancelled, negative, or duplicate records
4. **Feature engineering**: Create recency, frequency, monetary (RFM) features
5. **EDA**: Analyze customer behavior, product popularity, and temporal patterns