import pandas as pd

df = pd.read_csv("generated.csv", index_col=0)
print(df)

df1, df2, df3, df4 = df.iloc[:1500], df.iloc[1500:3000], df.iloc[3000:4500], df.iloc[4500:]


def process(df1, find, toind):
    df1['result'] = 2

    benefitList = pd.DataFrame()
    print(df1)

    for i in range(find, toind):
        if df1.benefit[i] == 1:
            if df1['math'][i] >= 120 and df1['ukr'][i] >= 120 and df1['eng'][i] >= 120 and df1['rating'][i] >= 144:
                benefitList = benefitList.append(df.iloc[i])
            else:
                df1['result'][i] = 0

    benefitList = benefitList.sort_values(by="rating", ascending=False)
    print(benefitList)

    benefits = len(benefitList)
    if benefits > 35:
        benefits = 35
    c = 0
    for row in benefitList.index:
        if c == benefits:
            break
        df1['result'][row] = 1
        c += 1

    free = 350 - benefits

    standartList = pd.DataFrame()
    for i in range(find, toind):
        if df1.benefit[i] == 1 and df1.result[i] == 2:
            df1.result[i] = 0
        if df1.benefit[i] == 0:
            if df1['math'][i] >= 140 and df1['rating'][i] >= 160:
                standartList = standartList.append(df.iloc[i])
            else:
                df1['result'][i] = 0

    standartList = standartList.sort_values(by="rating", ascending=False)
    print(standartList)

    standarts = len(standartList)
    if standarts > free:
        standarts = free
    c = 0
    for row in standartList.index:
        if c == standarts:
            break
        df1['result'][row] = 1
        c += 1

    for i in range(find, toind):
        if df1.benefit[i] == 0 and df1.result[i] == 2:
            df1.result[i] = 0

    print(df1[df1.result == 1].count().result)
    df1.to_csv(f'data{int(find / 1500)}.csv')


process(df1, 0, 1500)
process(df2, 1500, 3000)
process(df3, 3000, 4500)
process(df4, 4500, 6000)
