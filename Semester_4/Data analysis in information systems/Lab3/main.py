import matplotlib.pyplot as plt
import pandas as pd


def readDataset(path):
    data = pd.read_csv(path, encoding="Windows-1252", delimiter=';')
    return data


def fixIssues(data):
    data.rename(columns={"Populatiion": "Population"}, inplace=True)

    print(data.Region.unique())

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


def boxPlot(data, value):
    plt.figure()
    plt.title('Діаграма розмаху для ' + value)
    plt.boxplot(data[value])


def histogram(data, value):
    plt.figure()
    plt.title('Гістограма для ' + value)
    plt.hist(x=data[value])


def addColumn(data):
    data['Density'] = data['Population'] / data['Area']
    return data


def maxAverageArea(data):
    regions = data.Region.unique()
    maxVal, maxReg = 0, 0
    for i in regions:
        d = data[data.Region == i]
        if d.Area.mean() > maxVal:
            maxVal = d.Area.mean()
            maxReg = i
    return maxVal, maxReg


def maxDensity(data, region="world"):
    if region == "world":
        maxVal = data['Density'].max()
    else:
        maxVal = data[data.Region == region]['Density'].max()

    return maxVal, data[data['Density'] == maxVal]["Country Name"].iat[0]


def GDPbyRegions(data):
    regions = data.Region.unique()
    for i in regions:
        valMean = data[data.Region == i]['GDP per capita'].mean()
        valMedian = data[data.Region == i]['GDP per capita'].median()
        if abs(valMedian - valMean) <= min(valMedian, valMean) * 0.05:
            print(i, "`s average and median are equal with the values of", valMean, "and", valMedian)


if __name__ == '__main__':
    data = readDataset("Data2.csv")
    print(data.head())

    fixIssues(data)
    print(data)

    data = replaceBlank(data)
    print(data.head())

    print(data.info())

    boxPlot(data, 'GDP per capita')
    boxPlot(data, 'Population')
    boxPlot(data, 'CO2 emission')
    boxPlot(data, 'Area')

    histogram(data, 'GDP per capita')
    histogram(data, 'Population')
    histogram(data, 'CO2 emission')
    histogram(data, 'Area')
    plt.show()

    data = addColumn(data)
    print(data.head())

    print("The highest GDP per capita is in",
          data[data['GDP per capita'] == data['GDP per capita'].max()]["Country Name"].iat[0],
          "with the value of", data['GDP per capita'].max())
    print("\nThe country with the smallest area is", data[data['Area'] == data['Area'].min()]["Country Name"].iat[0],
          "with the value of", data['Area'].min())

    maxVal, maxArea = maxAverageArea(data)
    print("\nMaximum average area is", maxVal, "in", maxArea)

    maxVal, maxArea = maxDensity(data)
    print("\nMax density in the world is in", maxArea, "with the value of", maxVal)
    maxVal, maxArea = maxDensity(data, "Europe & Central Asia")
    print("\nMax density in Europe and Central Asia is in", maxArea, "with the value of", maxVal)

    GDPbyRegions(data)

    dataByGDP = data.sort_values("GDP per capita", ascending=False)
    print("\n", dataByGDP.head()[['Country Name', "GDP per capita"]], "\n",
          dataByGDP.tail()[['Country Name', "GDP per capita"]])

    dataByCo2 = data[::]
    dataByCo2["CO2 per capita"] = dataByCo2["CO2 emission"] / dataByCo2["Population"]
    dataByCo2 = dataByCo2.sort_values("CO2 per capita", ascending=False)
    print("\n", dataByCo2.head()[['Country Name', "CO2 per capita"]], "\n",
          dataByCo2.tail()[['Country Name', "CO2 per capita"]])

    dataByCo2.to_csv("dataByCo2.csv")
