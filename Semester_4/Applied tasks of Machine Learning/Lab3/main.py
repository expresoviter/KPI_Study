import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np

nyc = pd.read_csv("1895-2022.csv", skipfooter=4, engine="python")
nyc.columns = ["Date", "Temperature", "Anomaly"]
nyc.Date = nyc.Date.floordiv(100)
print("\n", nyc.head(), "\n")

xTrain, xTest, yTrain, yTest = train_test_split(nyc.Date.values.reshape(-1, 1),
                                                nyc.Temperature.values, random_state=11)

print(xTrain.shape)
print(xTest.shape)

linearRegression = LinearRegression()
linearRegression.fit(xTrain, yTrain)
print(linearRegression.coef_, linearRegression.intercept_)

predicted = linearRegression.predict(xTest)
expected = yTest
for p, e in zip(predicted[::5], expected[::5]):
    print(f'predicted {p:.2f}, expected {e:.2f}')

predict = (lambda x: linearRegression.coef_ * x + linearRegression.intercept_)
print(predict(2019))
print(predict(1890))

axes = sns.scatterplot(data=nyc, x='Date', y='Temperature', hue='Temperature', palette='winter', legend=False)
axes.set_ylim(10, 70)
x = np.array([min(nyc.Date.values), max(nyc.Date.values)])
y = predict(x)
print(x,y)
line = plt.plot(x, y)
plt.show()


