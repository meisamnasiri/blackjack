# blackjack
Resource Allocation Decision Engine That Takes Marketing Campaigns Performance Data And Suggest Budget Allocation For Maximizing Return on Investment Based on Past Results.


How much should we allocate budget on marketing campaigns, ads, discounts, etc.? Will this particular project generate enough revenue for it to be worthwhile? How much should we invest on our underdog products? These are the question of resource allocation under uncertainty. We cannot possibly know for certain if a particular investment will win, however we could guess the probability of a win and the amount of a win. Given these two, calculating expected return is simple math. But what is not simple is guessing correctly and allocating accordingly. Our Engine is expected to do just that. It decides on how much to allocate resource for a particular type of investment. It does this through feedback mechanisms for increasing ROI and adjusting expected returns based on average probabilities / returns of previous data. (metrics might change in subsequent versions.) The investment portfolio of companies for marketing, research, even human capital, etc. is sometimes overlooked. Companies forget that many of their decisions are made under uncertainties so systems of resource allocation are worthy considerations for any company.


Input:

CSV of campaigns performance (costs, conversions, revenue)

Output:

Recommended amount for each type of campaign channels (digital, tele, sms, email)

How to Run It:

```
python allocation_engine.py data.csv
```

Example:

Channel  | Cost  | Revenue | Conversions

Website  | 1000$ | 3000$   | 150
SMS      | 500$  | 1200$   | 60
Email    | 300$  | 800$    | 40


Channel   | Expected Return
Website → | 50% 
SMS     → | 30%
Email   → | 20% 