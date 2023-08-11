import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
import geopy.distance
from scipy import stats
import numpy as np

# Завдання 1 - пункт 1-2
cities = pd.read_csv("population.csv", delimiter=";")
cities = gpd.GeoDataFrame(cities, geometry=gpd.points_from_xy(cities.Longitude, cities.Latitude))

cityPopul = cities.copy()

ukraine = gpd.read_file("Ukraine/UKR_ADM1.shp")
fig, axis = plt.subplots(figsize=(10, 6))
axis.set_title("Population in 5 Ukrainian cities")
ukraine.plot(ax=axis)

cityPopul['Population'] /= 1000
cityPopul.plot(ax=axis, column="Population", markersize="Population", legend=True, alpha=0.5)
cities.plot(ax=axis, color='black')
for i in range(cities.shape[0]):
    axis.annotate(cities.City[i], xy=(cities.Longitude[i], cities.Latitude[i]))
plt.show()

# Завдання 1 - пункт 3
mapDist, kmDist, path = 0, 0, [0, 0, 0, 0]
for i in range(cities.shape[0]):
    city1 = (cities.Longitude[i], cities.Latitude[i])
    for j in range(i, cities.shape[0]):
        city2 = (cities.Longitude[j], cities.Latitude[j])
        mapS = ((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2) ** (1 / 2)
        if mapDist < mapS:
            mapDist = mapS
            path[0], path[1] = cities.City[i], cities.City[j]
        v = geopy.distance.geodesic(city1, city2)
        if v > kmDist:
            kmDist = v
            path[2], path[3] = cities.City[i], cities.City[j]
print("Maximum distance on the map is", mapDist, "between", path[0], "and", path[1])
print("Maximum distance in kilometers is", kmDist, "between", path[2], "and", path[3])


def fixIssues(data):
    for i in range(data.shape[0]):
        for j in range(2006, 2017):
            if not data[str(j)].isnull()[i]:
                data.loc[i, str(j)] = float(data.loc[i, str(j)].replace(',', '.'))


def regressOblast(data):
    for i in range(data.shape[0]):
        a = data.loc[i, :].values.tolist()
        a = a[2:]
        xList, yList = [], []
        for j in range(len(a)):
            if not np.isnan(a[j]):
                xList.append(2006 + j)
                yList.append(a[j])
        linearReg = stats.linregress(xList, yList)
        k = 0
        while linearReg.slope * (2006 + k) + linearReg.intercept < 0:
            k += 1
        for j in range(len(a)):
            if 2006 + j not in xList:
                data[str(2006 + j)][i] = linearReg.slope * (2006 + max(j, k)) + linearReg.intercept


# Завдання 3 - пункт 1
ukraine = gpd.read_file("Ukraine/UKR_ADM1.shp")
gdp = pd.read_csv("ukr_GDP.csv", encoding="cp1251", delimiter=";", skiprows=1)
income = pd.read_csv("ukr_DPP.csv", encoding="cp1251", delimiter=";", skiprows=1)
fixIssues(income)
regressOblast(gdp)
regressOblast(income)
print(gdp.head())
print(income.head())

# Завдання 3 - пункт 2
for i in range(2006, 2017):
    income[str(i)] = income[str(i)].astype(np.float64)
ukrGDP = ukraine.copy()
ukrGDP = ukrGDP.merge(gdp, how="left", on="Name")
fig, axis = plt.subplots(figsize=(10, 6))
axis.set_title("ВВП за регіонами в 2016 році")
ukrGDP.plot(ax=axis, column="2016", legend=True)
plt.show()

ukrDPP = ukraine.copy()
ukrDPP = ukrDPP.merge(income, how="left", on="Name")
fig, axis = plt.subplots(figsize=(10, 6))
axis.set_title("Прибуток населення на 1 особу в 2016 році")
ukrDPP.plot(ax=axis, column="2016", legend=True)
plt.show()

# Завдання 3 - пункт 3
fig, axis = plt.subplots(figsize=(10, 6))
axis.set_title("Кореляція між прибутком населення на 1 особу та ВВП")
correlation = income.loc[:, "2006":"2015"].corrwith(gdp.loc[:, "2006":"2015"], axis=1)
ukraine['Correlation'] = correlation
ukraine.plot(ax=axis, column='Correlation', legend=True)
plt.show()
