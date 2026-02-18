from data.loader import load_campaign_data

df = load_campaign_data("data/sampleCampaignData.csv")
print(df.groupby("campaign_id")[["spend", "revenue", "clicks", "conversions"]].sum())

print(df.dtypes)