import pandas as pd

def main():
    df = pd.read_csv('nba.csv')
    print(df)
    print(df.describe())



