import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import seaborn as sns
from kneed import KneeLocator


def readDataset(path):
    data = pd.read_csv(path, encoding="Windows-1252", delimiter=';')
    return data


def fixIssues(data):
    data.rename(columns={"Populatiion": "Population"}, inplace=True)

    for i in range(data.shape[0]):
        if not data['GDP per capita'].isnull()[i]:
            data.loc[i, 'GDP per capita'] = abs(float(data.loc[i, 'GDP per capita'].replace(',', '.')))
        if not data['Population'].isnull()[i]:
            data.loc[i, 'Population'] = abs(int(data.loc[i, 'Population']))
        if not data['CO2 emission'].isnull()[i]:
            data.loc[i, 'CO2 emission'] = abs(float(data.loc[i, 'CO2 emission'].replace(',', '.')))
        if not data['Area'].isnull()[i]:
            data.loc[i, 'Area'] = abs(float(data.loc[i, 'Area'].replace(',', '.')))


def replaceBlank(data):
    gdp, popul, co2, area = map(float, data.mean())
    popul = int(popul)
    for i in range(data.shape[0]):
        if data['GDP per capita'].isnull()[i]:
            data.loc[i, 'GDP per capita'] = gdp
        if data['Population'].isnull()[i]:
            data.loc[i, 'Population'] = popul
        if data['CO2 emission'].isnull()[i]:
            data.loc[i, 'CO2 emission'] = co2
        if data['Area'].isnull()[i]:
            data.loc[i, 'Area'] = area
    return data


def linearCheck(firstSet, secondSet):
    return abs(firstSet.corr(secondSet)) >= 0.8


data = readDataset("Data2.csv")
fixIssues(data)
data = replaceBlank(data)

data['GDP per capita'] = data['GDP per capita'].astype(np.float64)
data['CO2 emission'] = data['CO2 emission'].astype(np.float64)
data['Area'] = data['Area'].astype(np.float64)
data['Density'] = data['Population'] / data['Area']

print(data.head())

factors = ['GDP per capita', 'Population', 'CO2 emission', 'Area', 'Density']
kmeans_kwargs = {
    'init': 'random',
    'n_init': 10,
    'max_iter': 300,
    'random_state': 0,
}

sse = []
max_kernels = 10
for k in range(1, max_kernels + 1):
    kmeans = KMeans(n_clusters=k, **kmeans_kwargs)
    kmeans.fit(data[factors])
    sse.append(kmeans.inertia_)

plt.figure(figsize=(10, 8))
plt.plot(range(1, max_kernels + 1), sse)
plt.xticks(range(1, max_kernels + 1))
plt.xlabel('Number of Clusters')
plt.ylabel('SSE')
plt.grid(linestyle='--')
plt.show()
kl = KneeLocator(range(1, max_kernels + 1), sse, curve='convex', direction='decreasing')
print(f'Точка "ліктя": {kl.elbow}')

for i in range(2, 5):
    print(f"\nNumber of clusters is {i}")
    kmeans = KMeans(n_clusters=i, **kmeans_kwargs)
    kmeans.fit(data[factors])
    data[str(i)] = kmeans.labels_
    for j in range(i):
        print(f"\tCluster {j}")
        df = data[data[str(i)] == j]
        gdp = df[df['GDP per capita'] == df['GDP per capita'].max()]
        density = df[df['Density'] == df['Density'].max()]
        print(f"\t\tMax GDP per capita = {gdp.iloc[0, 2]} in {gdp.iloc[0, 1]}")
        print(f"\t\tMax Density = {density.iloc[0, 6]} in {density.iloc[0, 1]}")

for i in factors:
    plt.hist(data[i])
    plt.xlabel(i)
    plt.ylabel("Frequency")
    plt.show()

fig,axis=plt.subplots(figsize=(8,6))
sns.heatmap(data[factors].corr(numeric_only=True),ax=axis,annot=True)
plt.show()

print("Перевірка лінійної залежності між Population i CO2 Emission:",linearCheck(data.Population,data["CO2 emission"]))
print("Перевірка лінійної залежності між GDP per capita i Area:",linearCheck(data.Area,data["GDP per capita"]))