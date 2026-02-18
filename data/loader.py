import pandas as pd

required_columns = [
    "campaign_id",
    "date",
    "spend",
    "impressions",
    "clicks",
    "conversions",
    "revenue"
]

def load_campaign_data(file_path):
    try:
        df = pd.read_csv(file_path)
        missing_cols = [col for col in required_columns if col not in df.columns]
        if missing_cols:
            raise ValueError(f"Missing required columns: {missing_cols}")
        return df
    except Exception as e:
        print(f"Error loading campaign data: {e}")
        return None