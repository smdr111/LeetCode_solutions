import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'].loc[(employees['name'].str[0]=='M')|(employees['employee_id']%2==0)]=0
    employees['bonus']=employees['salary'].copy()
    return employees[['employee_id','bonus']].sort_values(by='employee_id')
    
