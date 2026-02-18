class CampaignData:
    def __init__(self, campaign_id, name, df):
        self.campaign_id = campaign_id
        self.name = name
        self.data = df

    def total_spend(self):
        return self.data["spend"].sum()
    def total_impressions(self):
        return self.data["impressions"].sum()
    def total_clicks(self):
        return self.data["clicks"].sum()
    def total_conversions(self):
        return self.data["conversions"].sum()
    def total_revenue(self):
        return self.data["revenue"].sum()
    
    