import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    data = teacher.groupby('teacher_id')['subject_id'].unique().reset_index()
    data['cnt'] = data['subject_id'].apply(lambda x: len(x))
    return data[['teacher_id','cnt']]

    
