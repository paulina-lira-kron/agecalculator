import pandas as pd
from rich import print

def add_full_name_column(df):
    """
    Creamos una nueva columna en el dataframe con el nombre completo de cada persona
    """
    df["full_name"] = df["first_name"] + " " + df["last_name"]
    return df