import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    immediate = delivery[delivery['order_date']==delivery['customer_pref_delivery_date']]
    percent = round(len(immediate)/len(delivery)*100,2)
    return pd.DataFrame({'immediate_percentage':[percent]})
