import pandas as pd
import statsmodels.tsa.api as smt
from main import dickey_fuller_test, plot_moving_average
from matplotlib import pyplot as plt
from sklearn.metrics import mean_squared_error


data = pd.read_csv("seattleWeather_1948-2017.csv", parse_dates=["DATE"], index_col=["DATE"])
print(data)

for i in range(data.shape[0]):
    data.TMAX[i] = (data.TMAX[i] - 32) / 1.8
    data.TMIN[i] = (data.TMIN[i] - 32) / 1.8

print(data.head())
print(data.RAIN.value_counts())
data['RAIN'] = data['RAIN'].fillna(False)
data['PRCP'] = data['PRCP'].fillna(0)

data['TAVG'] = (data.TMAX + data.TMIN) / 2
print(data.head())
print("Кореляція між температурою й наявністю опадів:",data['TAVG'].corr(data['RAIN']))
print("Кореляція між температурою й кількістю опадів:",data['TAVG'].corr(data['PRCP']))
dickey_fuller_test(data['PRCP'])

fig, ax = plt.subplots(figsize=(15, 10))
data['PRCP'].plot(ax=ax)
plt.show()

plot_moving_average(data['PRCP'][-365*3:],90,"PRCP")

model = smt.ARIMA(data['PRCP'], order=(1, 1, 1)).fit()
forecasts = model.forecast(365)
print(forecasts)
maxError=max([i-j for i,j in zip(data['PRCP'][-365:], forecasts)])
mse = mean_squared_error(data['PRCP'][-365:], forecasts)
print('MSE: %f' % mse)
print("Максимальна різниця між значенням 2017 і прогнозом 2018:",maxError)

