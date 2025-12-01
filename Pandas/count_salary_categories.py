import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    groups = ['Low Salary','Average Salary','High Salary']
    bins = [0,19999,50000,10000000000000]
    data = pd.cut(accounts.income,bins,labels=groups,include_lowest=True)
    return pd.DataFrame(data.value_counts().reset_index().set_axis(['category','accounts_count'],axis=1))
