from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

wine = load_wine()
x, y = wine.data, wine.target
print(type(x),y[0])

standardizer = StandardScaler()
xStd = standardizer.fit_transform(x)

xTrain, xTest, yTrain, yTest = train_test_split(xStd, y, random_state=4)

knn = KNeighborsClassifier(n_neighbors=5, n_jobs=-1).fit(xTrain, yTrain)
svc = SVC(kernel="linear").fit(xTrain, yTrain)
bayes = GaussianNB().fit(xTrain, yTrain)

knnPredict = knn.predict(xTest)
svcPredict = svc.predict(xTest)
bayesPredict = bayes.predict(xTest)

correct = [0, 0, 0]
for i in range(len(knnPredict)):
    if knnPredict[i] == yTest[i]:
        correct[0] += 1
    if svcPredict[i] == yTest[i]:
        correct[1] += 1
    if bayesPredict[i] == yTest[i]:
        correct[2] += 1
print("Predictions are correct in", correct[0] / len(knnPredict) * 100, "% of cases for KNN")
print("Predictions are correct in", correct[1] / len(knnPredict) * 100, "% of cases for SVC")
print("Predictions are correct in", correct[2] / len(knnPredict) * 100, "% of cases for GaussianNB")
