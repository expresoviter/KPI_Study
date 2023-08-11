import pandas as pd
import numpy as np
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

titanic = pd.read_csv("titanic.csv")
print(titanic.head())
print(titanic["Cabin"].isna().sum())
factors = ["Survived", "Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]
data = titanic[factors]

ageMean = data.Age.mean()
print("S counts =", data.Embarked.value_counts()["S"])
print("C counts =", data.Embarked.value_counts()["C"])
print("Q counts =", data.Embarked.value_counts()["Q"])

for i in range(data.shape[0]):
    if data.Age.isnull()[i]:
        data.loc[i, "Age"] = ageMean
    if data.Embarked.isnull()[i] or data.Embarked[i] == "S":
        data.loc[i, "Embarked"] = 1
    elif data.Embarked[i] == "C":
        data.loc[i, "Embarked"] = 2
    else:
        data.loc[i, "Embarked"] = 3
    if data.Sex[i] == "male":
        data.loc[i, "Sex"] = 0
    else:
        data.loc[i, "Sex"] = 1

for i in factors:
    data[i] = data[i].astype(np.float64)
print(data)

fig, axis = plt.subplots(figsize=(8, 6))
sns.heatmap(data.corr(), ax=axis, annot=True)
plt.show()

for row, factor in enumerate(factors[1:]):
    if factor != "Sex":
        plot = sns.FacetGrid(data[["Sex", "Survived"] + [factor]], col="Sex", hue="Survived")
        plot.map(sns.histplot, factor)
        plot.add_legend()
plt.show()

y = data["Survived"]
x = data[factors[1:]]

x = StandardScaler().fit_transform(x)
kmeans = KMeans(n_clusters=2, max_iter=500, algorithm="lloyd", random_state=1)
kmeans.fit(x)
predictKmeans = kmeans.predict(x)

agglomerative = AgglomerativeClustering(n_clusters=2, affinity="euclidean", linkage="ward")
predictAglo = agglomerative.fit_predict(x)

X_train, X_test, y_train, y_test = train_test_split(x, y, random_state=4)
kneighbors = KNeighborsClassifier(n_neighbors=5, n_jobs=-1).fit(X_train, y_train)
predictKnn = kneighbors.predict(X_test)

ck, ca = 0, 0
for i in range(len(y)):
    if y[i] == predictKmeans[i]:
        ck += 1
    if y[i] == predictAglo[i]:
        ca += 1
print(f"K-Means Clustering effectivity = {ck / len(y) * 100}%")
print(f"Agglomerative Clustering effectivity = {ca / len(y) * 100}%")
print(f"KNN Classifier effectivity = {kneighbors.score(X_test, y_test) * 100}%")
