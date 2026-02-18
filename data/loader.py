from typing import Dict
import pandas as pd
from core.campaign import Campaign

REQUIRED_COLUMNS = [
    "campaign_id",
    "date",
    "spend",
    "impressions",
    "clicks",
    "conversions",
    "revenue"
]

NUMERIC_COLUMNS = [
    "spend",
    "impressions",
    "clicks",
    "conversions",
    "revenue"
]

def load_campaign_data(file_path: str) :
   
    df = pd.read_csv(file_path)
    df = validate_campaign_data(df)
    
    return df
    


def validate_campaign_data(df: pd.DataFrame) -> pd.DataFrame:
    missing_cols = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing required columns: {missing_cols}")
    
    df["date"] = pd.to_datetime(df["date"], errors="raise")

    for col in NUMERIC_COLUMNS:
        df[col] = pd.to_numeric(df[col], errors="raise")

    df["spend"] = df["spend"].astype(float)
    df["impressions"] = df["impressions"].astype(int)
    df["clicks"] = df["clicks"].astype(int)
    df["conversions"] = df["conversions"].astype(int)
    df["revenue"] = df["revenue"].astype(float)

    # Sanity checks
    if (df["spend"] < 0).any():
        raise ValueError("Spend cannot be negative")

    if (df["clicks"] > df["impressions"]).any():
        raise ValueError("Clicks cannot exceed impressions")

    if (df["conversions"] > df["clicks"]).any():
        raise ValueError("Conversions cannot exceed clicks")

    return df