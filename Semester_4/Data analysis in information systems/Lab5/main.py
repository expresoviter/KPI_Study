import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt


def effectivity(name, regression, xTrain, yTrain, xTest, yTest):
    predictTrain = regression.predict(xTrain)
    predictTest = regression.predict(xTest)
    errorTrain = mean_absolute_error(predictTrain, yTrain)
    errorTest = mean_absolute_error(predictTest, yTest)
    print("Mean absolute error is", errorTrain, "for", name, "regression train data.")
    print("Mean absolute error is", errorTest, "for", name, "regression test data.\n")
    fig, axis = plt.subplots(1, 2, figsize=(10, 6))
    axis[0].set_title(name + ' regression')
    for i in ((0, 'train'), (1, 'test')):
        axis[i[0]].set_xlabel('Prediction for ' + i[1] + ' data')
        axis[i[0]].set_ylabel(i[1] + ' data values')
        axis[i[0]].axline([0, 0], [1, 1], color='green')
    axis[0].scatter(predictTrain, yTrain)
    axis[1].scatter(predictTest, yTest)
    plt.show()


if __name__ == "__main__":
    wine = pd.read_csv("winequality-red.csv")
    print(wine.head())
    x, y = [], []
    for i in range(wine.shape[0]):
        a = wine.iloc[i].values
        x.append(a[:-1])
        y.append(a[-1])
    xTrain, xTest, yTrain, yTest = train_test_split(x, y, random_state=11)

    linRegress = LinearRegression().fit(xTrain, yTrain)
    effectivity("linear", linRegress, xTrain, yTrain, xTest, yTest)

    for i in range(1, 4):
        polFeat = PolynomialFeatures(degree=i, include_bias=False)
        xPolyTrain = polFeat.fit_transform(xTrain)
        polRegress = LinearRegression().fit(xPolyTrain, yTrain)

        xPolyTrain1 = polFeat.transform(xTrain)
        xPolyTest = polFeat.transform(xTest)

        effectivity("polynomial " + str(i), polRegress, xPolyTrain, yTrain, xPolyTest, yTest)
