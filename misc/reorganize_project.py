
import shutil
import os
from pathlib import Path

# Paths
ROOT = Path(r"c:\Users\sagar\Desktop\data_YourNextPurchase")
DATA_DIR = ROOT / "data"
RAW_FILE = DATA_DIR / "raw"
DATA_RAW_DIR = DATA_DIR / "raw_data" # Temp name to avoid conflict
FINAL_RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
CLEANED_DIR = ROOT / "cleaned_data"
EDA_OUTPUTS = ROOT / "eda_outputs"
MARKETING_DIR = ROOT / "marketing"
MARKETING_EDA = MARKETING_DIR / "eda_outputs"
MISC_DIR = ROOT / "misc"
MODELS_DIR = ROOT / "models"
DASHBOARD_DIR = ROOT / "dashboard"

# Ensure base directories exist
MARKETING_EDA.mkdir(parents=True, exist_ok=True)
MISC_DIR.mkdir(parents=True, exist_ok=True)
(MODELS_DIR / "new_customer").mkdir(parents=True, exist_ok=True)
(MODELS_DIR / "repurchase").mkdir(parents=True, exist_ok=True)
DASHBOARD_DIR.mkdir(parents=True, exist_ok=True)

print(f"Reorganizing {ROOT}...")

# 0. FIX BROKEN 'raw' FILE
if RAW_FILE.exists() and not RAW_FILE.is_dir():
    print("Found 'raw' file (improperly named clients.csv). Renaming...")
    try:
        shutil.move(str(RAW_FILE), str(DATA_DIR / "clients.csv"))
        print("Restored clients.csv")
    except Exception as e:
        print(f"Error restoring clients.csv: {e}")

# 1. Create Raw Directory
FINAL_RAW_DIR.mkdir(parents=True, exist_ok=True)

# 2. Move raw CSVs from data/ to data/raw/
for csv_file in DATA_DIR.glob("*.csv"):
    if csv_file.parent == DATA_DIR: 
        try:
            shutil.move(str(csv_file), str(FINAL_RAW_DIR / csv_file.name))
            print(f"Moved {csv_file.name} to data/raw/")
        except Exception as e:
            print(f"Error moving {csv_file.name}: {e}")

# 3. Move cleaned data to data/processed/
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
if CLEANED_DIR.exists():
    for csv_file in CLEANED_DIR.glob("*.csv"):
        try:
            shutil.move(str(csv_file), str(PROCESSED_DIR / csv_file.name))
            print(f"Moved {csv_file.name} to data/processed/")
        except Exception as e:
             print(f"Error moving {csv_file.name}: {e}")
    # Remove empty dir
    try:
        CLEANED_DIR.rmdir()
        print("Removed cleaned_data/ directory")
    except:
        print("cleaned_data/ not empty, skipping removal")

# 4. Move EDA outputs
if EDA_OUTPUTS.exists():
    for f in EDA_OUTPUTS.glob("*"):
        try:
            shutil.move(str(f), str(MARKETING_EDA / f.name))
            print(f"Moved {f.name} to marketing/eda_outputs/")
        except Exception as e:
             print(f"Error moving {f.name}: {e}")
    # Remove empty dir
    try:
        EDA_OUTPUTS.rmdir()
        print("Removed eda_outputs/ directory")
    except:
        print("eda_outputs/ not empty, skipping removal")
        
# 5. Move script files to misc
scripts_to_move = [
    "data_preparation_final.py", 
    "validate_data.py", 
    "generate_report.py", 
    "01_data_preparation.py", 
    "02_data_quality_report.py",
    "extract_ppt.py",
    "ppt_content.txt",
    "FILES_TO_SHARE.md",
    "DATA_PREPARATION_SUMMARY.md",
    "data_preparation_report.md",
    "EDA_SUMMARY.md"
]

for script in scripts_to_move:
    script_path = ROOT / script
    if script_path.exists():
        try:
            shutil.move(str(script_path), str(MISC_DIR / script))
            print(f"Moved {script} to misc/")
        except Exception as e:
            print(f"Error moving {script}: {e}")

# 6. Move EDA script to marketing
eda_script = ROOT / "exploratory_analysis.py"
if eda_script.exists():
    try:
        shutil.move(str(eda_script), str(MARKETING_DIR / "exploratory_analysis.py"))
        print("Moved exploratory_analysis.py to marketing/")
    except Exception as e:
        print(f"Error moving exploratory_analysis.py: {e}")

print("Reorganization complete!")
