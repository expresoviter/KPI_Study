import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.read_csv("https://vincentarelbundock.github.io/Rdatasets/csv/carData/TitanicSurvival.csv")
print(titanic.head())
print(titanic.tail())

titanic.rename(columns={"Unnamed: 0": "name", "passengerClass": "class"}, inplace=True)
print(titanic.head())

print("Min age: ", titanic["age"].min())
print("Max age: ", titanic["age"].max())
print("Average age: ", titanic["age"].mean())

print(titanic[titanic["survived"] == "yes"].describe())

fem1 = titanic[(titanic["sex"] == "female") & (titanic["class"] == "1st")]
print(fem1.head())
print("Min age =",fem1["age"].min(), ";\nMax age =",fem1["age"].max(), "\n", fem1[fem1["survived"] == "yes"].count())

histogram = titanic.hist()
plt.show()
