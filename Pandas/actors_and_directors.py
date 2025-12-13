import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    groups = actor_director.groupby(["actor_id", "director_id"])
    cnt = groups['timestamp'].count()
    ans = cnt[cnt>=3]
    return ans.reset_index()[['actor_id','director_id']]


    
