import pandas as pd


def main():
    df = pd.read_csv("nba.csv")
    print(df)
    print(df.describe())
    print("median of age: " + str(df["Age"].median()))
    print("median of weight: " + str(df["Weight"].median()))
    print("median of salary: " + str(df["Salary"].median()))


main()
