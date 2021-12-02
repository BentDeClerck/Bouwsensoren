import pandas as pd
import os
import csv

def openfile(date):
    try:
        df = pd.read_csv(f'../Bouwsensoren/Website/dates/{date}')
        return(df)
    except:
        return('file not found')
    print(df)


