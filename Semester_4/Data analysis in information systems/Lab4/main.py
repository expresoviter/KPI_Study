import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.stats as stats


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


def normalityTest(data, test, alpha=0.05):
    stat, p = test(data)
    print('\tStatistics = %.3f, p = %.3f' % (stat, p))
    if p > alpha:
        print('\tДані відповідають нормальному розподілу (нульова гіпотеза H0 не відкидається)')
    else:
        print('\tДані не відповідають нормальному розподілу (нульова гіпотеза H0 відкидається)')


def checkMeanMedianEquality(data, alpha=0.05):
    for i in ["GDP per capita", "Population", "CO2 emission", "Area"]:
        mean, median = data[i].mean(), data[i].median()
        stat, p = stats.ttest_1samp(a=data[i], popmean=median)
        if p < alpha:
            print("\nMean and Median are not equal for", i)
        else:
            print("Mean and Median are equal for", i)
        print("\tMean =", mean)
        print("\tMedian =", median)


if __name__ == '__main__':
    # Пункт 1
    data = readDataset("Data2.csv")
    fixIssues(data)
    data = replaceBlank(data)

    data['GDP per capita'] = data['GDP per capita'].astype(np.float64)
    data['CO2 emission'] = data['CO2 emission'].astype(np.float64)
    data['Area'] = data['Area'].astype(np.float64)

    print(data.head())
    print(data.info())
    print(data.describe())

    # Пункт 2:
    data.hist(figsize=(10, 10))
    plt.show()

    print()
    for i in ['GDP per capita','Population','CO2 emission','Area']:
        print(i+":")
        normalityTest(data[i], stats.shapiro)

    # Пункт 3
    checkMeanMedianEquality(data)

    # Пункт 4
    data['CO2 emission'].hist(by=data['Region'], layout=(4, 2), figsize=(10, 20))
    plt.show()
    regions = pd.unique(data['Region'])

    for region in regions:
        regionEmissions = data[data['Region'] == region]['CO2 emission']
        print(f'\nПеревірка для регіону {region}:')
        print(f'Критерій Shapiro-Wilk:')
        try:
            normalityTest(regionEmissions, stats.shapiro)
        except ValueError as e:
            print(str(e))

    # Пункт 5
    fig, ax = plt.subplots(figsize=(8, 8))
    labels = pd.unique(data['Region'])
    wedges, texts, autotexts = ax.pie(data.groupby('Region').sum()['Population'], labels=labels, autopct='%1.1f%%',
                                       textprops=dict(color='w'))

    ax.set_title('Населення за регіонами')
    legend=ax.legend(wedges, [1,2,3,4,5,6,7],
              title='Регіони',
              loc='center left',
              bbox_to_anchor=(1, 0, 0, 1))
    plt.setp(autotexts, size=12, weight='bold')
    plt.show()
    fig.savefig('piechart', bbox_extra_artists=(legend,), bbox_inches='tight')
