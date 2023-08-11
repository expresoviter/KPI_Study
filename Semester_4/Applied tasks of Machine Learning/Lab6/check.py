import pandas as pd


def check(df1, find, toind):
    benefit, normal = 0, 0
    for i in range(find, toind):
        if df1.benefit[i] == 1 and df1['math'][i] >= 120 and df1['ukr'][i] >= 120 and df1['eng'][i] >= 120 and \
                df1['rating'][i] >= 144:
            benefit += 1
        elif df1.benefit[i] == 0 and df1['math'][i] >= 140 and df1['rating'][i] >= 160:
            normal += 1
    return benefit, normal


data = pd.read_csv("data1.csv", index_col=0)
b, n = check(data, 1500, 3000)
print(b, n)
