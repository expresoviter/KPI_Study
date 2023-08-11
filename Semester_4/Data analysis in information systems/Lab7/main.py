import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.tsa.api as smt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf, plot_predict


def plot_moving_average(series, n, country):
    rolling_mean = series.rolling(window=n).mean()
    plt.figure(figsize=(15, 5))
    plt.title(f'Moving average\n window size = {n} for {country}')
    plt.plot(rolling_mean, c='orange', label='Rolling mean trend')
    plt.plot(series[n:], label='Actual values')
    plt.legend(loc='upper left')
    plt.grid(True)
    plt.show()


def dickey_fuller_test(series):
    test = smt.adfuller(series, autolag='AIC')
    print('adf: ', test[0])
    print('p-value: ', test[1])
    print('Critical values: ', test[4])
    if test[0] > test[4]['5%']:
        print('Наявні одиничні корені, ряд не стаціонарний.')
    else:
        print('Одиничні корені відсутні, ряд є стаціонарним.')


if __name__ == '__main__':
    covid = pd.read_csv("owid-covid-data.csv", parse_dates=['date'], index_col=['date'])
    factors = ["location", "total_cases", "new_cases", "total_deaths", "new_deaths"]
    data = covid[factors]
    print(data)

    fig, ax = plt.subplots(figsize=(15, 10))

    germanyCovid = data[data.location == 'Germany'].new_cases
    polandCovid = data[data.location == 'Poland'].new_cases
    germanyCovid.plot(ax=ax)
    polandCovid.plot(ax=ax)
    plt.title('Часова динаміка Covid в Німеччині та Польщі')
    ax.grid()
    plt.legend(['Germany', 'Poland'])
    plt.show()

    print(germanyCovid.describe())
    germanyCovid.hist(figsize=(12, 8))
    plt.title('Частота кількости випадків в Німеччині')
    plt.show()

    print(polandCovid.describe())
    polandCovid.hist(figsize=(12, 8))
    plt.title('Частота кількости випадків в Польщі')
    plt.show()

    plot_moving_average(germanyCovid, 30, 'Germany')
    plot_moving_average(polandCovid, 30, 'Poland')

    smt.seasonal_decompose(germanyCovid[~germanyCovid.isna()]).plot().set_size_inches(15, 10)
    plt.show()

    smt.seasonal_decompose(polandCovid[~polandCovid.isna()]).plot().set_size_inches(15, 10)
    plt.show()

    fig, ax = plt.subplots(4, figsize=(15, 10))
    ax[0] = plot_acf(germanyCovid[~germanyCovid.isna()], ax=ax[0], lags=120)
    ax[1] = plot_pacf(germanyCovid[~germanyCovid.isna()], ax=ax[1], lags=120)
    ax[2] = plot_acf(polandCovid[~polandCovid.isna()], ax=ax[2], lags=120)
    ax[3] = plot_pacf(polandCovid[~polandCovid.isna()], ax=ax[3], lags=120)
    plt.show()

    print("Germany:")
    dickey_fuller_test(germanyCovid[~germanyCovid.isna()])
    print("\nPoland:")
    dickey_fuller_test(polandCovid[~polandCovid.isna()])

    print("Correlation:", germanyCovid.corr(polandCovid))

    kurs = pd.read_csv("kurs-uah-eur.csv", parse_dates=["Date"], index_col=["Date"], dayfirst=True)
    print(kurs)
    fig, ax = plt.subplots(figsize=(15, 10))
    ax.plot(kurs['Value'])
    plt.show()

    plot_moving_average(kurs['Value'], 30, "UAH-EUR")

    price_decomposition = smt.seasonal_decompose(kurs['Value'])
    fig = price_decomposition.plot()
    fig.set_size_inches(15, 10)
    plt.show()

    fig, ax = plt.subplots(2, figsize=(15, 10))
    ax[0] = plot_acf(kurs['Value'], ax=ax[0], lags=100)
    ax[1] = plot_pacf(kurs['Value'], ax=ax[1], lags=100)
    plt.show()

    dickey_fuller_test(kurs['Value'])
    kursDiff = kurs['Value'].diff(periods=1).dropna()
    dickey_fuller_test(kursDiff)
    fig, ax = plt.subplots(2, figsize=(15, 10))
    ax[0] = plot_acf(kursDiff, ax=ax[0], lags=100)
    ax[1] = plot_pacf(kursDiff, ax=ax[1], lags=100)

    train_data = kurs['Value'][:-7]
    model = smt.ARIMA(train_data, order=(1, 1, 1)).fit()
    print(model.summary())

    pred = model.predict(kurs['Value'].index[-7], kurs['Value'].index[-1])
    fig, ax = plt.subplots(figsize=(15, 10))
    kurs['Value'][-20:].plot(ax=ax)
    ax.vlines(kurs['Value'].index[-7], 35, 45, linestyle='--', color='r', label='Start of forecast')
    ax = plot_predict(model, kurs['Value'].index[-7], kurs['Value'].index[-1], dynamic=True, plot_insample=False, ax=ax)
    plt.show()

    forecasts = model.forecast(7)
    print(forecasts)
