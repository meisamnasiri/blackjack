import pandas as pd 

class Campaign:
    def __init__(self, campaign_id: str, df: pd.DataFrame):
        self.campaign_id = campaign_id
        self.data = df.sort_values("date")

    def total_spend(self) -> float:
        return self.data["spend"].sum()
    
    def total_impressions(self) -> int:
        return self.data["impressions"].sum()
    
    def total_clicks(self) -> int:
        return self.data["clicks"].sum()
    
    def total_conversions(self) -> int:
        return self.data["conversions"].sum()
    
    def total_revenue(self) -> float:
        return self.data["revenue"].sum()
    
    def profit(self) -> float:
        return self.total_revenue() - self.total_spend()
    
    def roi(self) -> float:
        spend = self.total_spend()
        if spend == 0:
            return 0.0
        return self.profit() / spend

    # Click-Through Rate
    def ctr(self) -> float:
        impressions = self.total_impressions()
        return self.total_clicks() / impressions if impressions > 0 else 0.0
    
    # Cost Per Click
    def cpc(self) -> float:
        clicks = self.total_clicks()
        return self.total_spend() / clicks if clicks > 0 else 0.0
    
    # Cost Per Conversion
    def ccv(self) -> float:
        conversions = self.total_conversions()
        return self.total_spend() / conversions if conversions > 0 else 0.0
    
    # Conversion Rate
    def cvr(self) -> float:
        clicks = self.total_clicks()
        return self.total_conversions() / clicks if clicks > 0 else 0.0
    
    # revenue per conversion
    def rcv(self) -> float:
        return self.total_revenue() / self.total_conversions() if self.total_conversions() > 0 else 0.0
    
    def summary(self) -> dict:
        return {
            "campaign_id": self.campaign_id,
            "spend": self.total_spend(),
            "revenue": self.total_revenue(),
            "profit": self.profit(),
            "roi": self.roi(),
            "ctr": self.ctr(),
            "cvr": self.cvr(),
            "rcv": self.rcv(),
        }