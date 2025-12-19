import pandas as pd

def account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    df = users.merge(transactions,on='account').groupby(['name','account'])['amount'].sum().reset_index()
    df.columns = df.columns.str.upper()
    return df[df.AMOUNT>10000].drop('ACCOUNT',axis=1).rename(columns={'AMOUNT':'BALANCE'})
    
    
