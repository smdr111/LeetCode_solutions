import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    result = person.groupby('email').count().reset_index()
    result.rename(columns={'email':'Email'},inplace=True)
    return result[result['id']>1][['Email']]
    
