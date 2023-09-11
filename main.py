import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv("nba.csv")
    print(df)
    print(df.describe())
    print("median of age: " + str(df["Age"].median()))
    print("median of weight: " + str(df["Weight"].median()))
    print("median of salary: " + str(df["Salary"].median()))
    # x = df['Name']
    # df['Age'] = df['Age'].astype(str)
    # # print(type(y))
    # plt.bar(x, df['Age'])
    # plt.xlabel('X轴标签')
    # plt.ylabel('Y轴标签')
    # plt.title('柱状图示例')
    # plt.show()

    plt.figure(figsize=(10, 6))
    plt.hist(df["Age"], bins=20, edgecolor="black")
    plt.title("Shape_Leng Distribution")
    plt.xlabel("Shape_Leng")
    plt.ylabel("Count")
    plt.show() 
    # plt.plot(df["Name"], df["Age"])
    # plt.show()


main()
