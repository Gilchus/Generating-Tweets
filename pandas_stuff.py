import pandas as pd

def list_to_df(list):
    df = pd.DataFrame(list, columns=["tweets"])
    return df