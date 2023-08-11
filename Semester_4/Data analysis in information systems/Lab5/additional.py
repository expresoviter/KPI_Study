import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from main import effectivity
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


def fixIssues(df1):
    for i in range(df1.shape[0]):
        for j in range(3, 7):
            df1.iat[i, j] = float(df1.iat[i, j].replace(',', '.'))
    valueNames = ['Cql', 'Ie', 'Iec', 'Is']
    for i in valueNames:
        df1[i] = df1[i].astype(np.float64)


def getRegressValues(df):
    x, y = [], []
    for i in range(df.shape[0]):
        a = df.iloc[i].values
        x.append(a[3:-1])
        y.append(a[-1])
    return x, y


if __name__ == "__main__":
    df1 = pd.read_csv("Data4.csv", encoding="cp1251", delimiter=";")
    df2 = pd.read_csv("Data4t.csv", encoding="cp1251", delimiter=";")
    print(df1.head())
    print(df2.head())
    fixIssues(df1)
    fixIssues(df2)
    print(df1.head())
    print(df2.head())
    correlation=df1.corr(numeric_only=True)
    print(correlation)
    print("Визначник кореляційної матриці:",np.linalg.det(correlation.to_numpy()))

    fig, axes = plt.subplots(2, 3, figsize=(16, 8))
    c = 0
    valueNames = ['Cql', 'Ie', 'Iec', 'Is']
    for i in range(len(valueNames) - 1):
        for j in range(i + 1, len(valueNames)):
            axes[c // 3][c % 3].set_title("Діаграма розсіювання для " + valueNames[i] + " i " + valueNames[j])
            axes[c // 3][c % 3].set_xlabel(valueNames[i])
            axes[c // 3][c % 3].set_ylabel(valueNames[j])
            axes[c // 3][c % 3].scatter(df1[valueNames[i]], df1[valueNames[j]])
            c += 1
    plt.show()

    xTrain, yTrain = getRegressValues(df1)
    xTest, yTest = getRegressValues(df2)

    linRegress = LinearRegression().fit(xTrain, yTrain)
    effectivity("linear", linRegress, xTrain, yTrain, xTest, yTest)

    for i in range(2, 4):
        polFeat = PolynomialFeatures(degree=i, include_bias=False)
        xPolyTrain = polFeat.fit_transform(xTrain)
        polRegress = LinearRegression().fit(xPolyTrain, yTrain)

        xPolyTest = polFeat.transform(xTest)

        effectivity("polynomial " + str(i), polRegress, xPolyTrain, yTrain, xPolyTest, yTest)
