import pandas as pd
from age_calculator import open_csv_data, get_df_fixed_data
from datetime import datetime
from rich import print


def main():
    #start the program
    print("Bienvenido a la calculadora de edad")

    #get csv data
    df = open_csv_data()
    print(df)

    #get df fixed data
    df = get_df_fixed_data(df)
    print("La edad de cada persona es:")
    print(df)




if __name__ == "__main__":
    main()
