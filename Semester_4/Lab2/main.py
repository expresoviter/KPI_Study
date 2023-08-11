import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy import stats

nyc = pd.read_csv("1895-2022.csv", skipfooter=4, engine="python")
print(nyc.head())

nyc.columns = ["Date", "Temperature", "Anomaly"]
print("\n", nyc.head())
nyc.Date = nyc.Date.floordiv(100)
print("\n", nyc.head(), "\n")
pd.set_option('display.precision', 2)
print(nyc.Temperature.describe(), "\n")

sns.set_style("whitegrid")
pair = sns.pairplot(data=nyc, y_vars=["Temperature", "Anomaly"], x_vars=["Date"], kind="reg")
plt.show()

linearRegression = stats.linregress(x=nyc.Date, y=nyc.Temperature)
forecast = [linearRegression.slope * i + linearRegression.intercept for i in range(2019, 2023)]
[print("January", i + 2019, "forecast:", forecast[i]) for i in range(4)]

beforeCast = [linearRegression.slope * i + linearRegression.intercept for i in range(1890, 1895)]
[print("January", i + 1890, "forecast:", beforeCast[i]) for i in range(5)]

'''axes = sns.regplot(x=nyc.Date, y=nyc.Temperature)
plt.show()'''
axesWLim = sns.regplot(x=nyc.Date, y=nyc.Temperature)
axesWLim.set_ylim(10, 70)
plt.show()
