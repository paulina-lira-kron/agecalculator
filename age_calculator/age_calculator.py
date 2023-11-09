from datetime import datetime
from rich import print
import pandas as pd

def open_csv_data():
#Abrimos el archivo csv con los datos de las personas
    
    #open csv file
    try:
        df = pd.read_csv("data/people.csv")
        return df
    except FileNotFoundError:
        print("[red]No se ha encontrado el archivo[/red]")
        exit()

def get_df_fixed_data(df):
    """
    Creamos una nueva columna en el dataframe con la edad de cada persona
    """
    df["age"] = df["birthday"].apply(lambda x: get_age(x))
    return df

def get_age(birthday):
    """
    Calculamos la edad a partir de la fecha de nacimiento
    """
    #get today's date
    today = datetime.today()

    #get birthday date
    birthday_date = datetime.strptime(birthday, "%m/%d/%Y")

    #calculate age
    age = today.year - birthday_date.year

    #return age
    return age
