# Mission_6_11 - The Next Purchase
**Hackathon Case Study: Centrale-ESSEC Data Challenge 2026**

## 🎯 Project Overview
We are building an AI-powered product recommendation system and business dashboard for a sports retail client.

## 📁 Repository Structure

```
Mission_6_11/
├── data/                       # Data (Gitignored - DO NOT COMMIT CSVs)
│   ├── raw/                    # Original datasets
│   └── processed/              # Cleaned & featured datasets
│
├── marketing/                  # Marketing Analysis
│   ├── exploratory_analysis.py # EDA Script
│   └── eda_outputs/            # Generated charts & insights
│
├── models/                     # Machine Learning Models
│   ├── new_customer/           # Acquisition models
│   └── repurchase/             # Retention models
│
├── dashboard/                  # Streamlit/Dash App
│
├── misc/                       # Utilities & Reports
│   ├── data_preparation_final.py
│   ├── validation_data.py
│   └── ...
│
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## 🚀 Getting Started

1.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Data Setup**
    - Ensure `data/raw/` contains the 5 original CSV files.
    - Run the cleaning script if `data/processed/` is empty:
      ```bash
      python misc/data_preparation_final.py
      ```

3.  **Run EDA**
    ```bash
    python marketing/exploratory_analysis.py
    ```

## 📊 Status
- ✅ **Data Prep**: Complete (see `misc/DATA_PREPARATION_SUMMARY.md`)
- ✅ **EDA**: Complete (see `misc/EDA_SUMMARY.md`)
- 🚧 **Models**: In Progress
- 🚧 **Dashboard**: Planned

## 👥 Team
**Mission_6_11**
