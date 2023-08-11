from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
import matplotlib.pyplot as plt

digits = load_digits()
print("Дані 36 цифри в наборі:")
print(digits.images[35])

figure, axes = plt.subplots(6, 6, figsize=(6, 6))
for item in zip(axes.ravel(), digits.images[:36], digits.target[:36]):
    axes, image, target = item
    axes.imshow(image, cmap=plt.cm.gray_r)
    axes.set_xticks([])
    axes.set_yticks([])
    axes.set_title(target)
plt.tight_layout()
plt.show()

X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, random_state=11)
print(f'\nСтандартне розділення вибірки 75 на 25%: Train - {X_train.shape}, test - {X_test.shape}')

X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, random_state=11, test_size=0.20)
print(f'Розділення вибірки 80 на 20%: Train - {X_train.shape}, test - {X_test.shape}\n')

knn = KNeighborsClassifier()
knn.fit(X_train, y_train)

predicted = knn.predict(X_test)

print(f'Передбачені значення за KNN (K=5): {predicted[:36]}')
print(f'Очікувані значення за KNN (K=5)  : {y_test[:36]}')

print(f'Оцінка KNN (K=5) = {knn.score(X_test, y_test):.2%}')

confusion = confusion_matrix(y_true=y_test, y_pred=predicted)
print(f'\nМатриця невідповідностей для KNN (K=5):\n{confusion}')

names = [str(digit) for digit in digits.target_names]
print('\nЗвіт класифікації для KNN (K=5):\n', classification_report(y_test, predicted, target_names=names))

svc = SVC(kernel="rbf").fit(X_train, y_train)
bayes = GaussianNB().fit(X_train, y_train)
svcPredict = svc.predict(X_test)
bayesPredict = bayes.predict(X_test)
print(f'Оцінка SVC = {svc.score(X_test, y_test):.2%}')
print(f'Оцінка GaussianNB = {bayes.score(X_test, y_test):.2%}')

confusionSVC = confusion_matrix(y_true=y_test, y_pred=svcPredict)
print('\nЗвіт класифікації для SVC:\n', classification_report(y_test, svcPredict, target_names=names))

confusionBayes = confusion_matrix(y_true=y_test, y_pred=bayesPredict)
print('\nЗвіт класифікації для GaussianNB:\n', classification_report(y_test, bayesPredict, target_names=names))

for i in range(2, 11):
    if i == 5:
        print(f'Оцінка KNN (K=5) = {knn.score(X_test, y_test):.2%}')
    else:
        knnRange = KNeighborsClassifier(n_neighbors=i, n_jobs=-1)
        knnRange.fit(X_train, y_train)
        predicted = knnRange.predict(X_test)
        print(f'Оцінка KNN (K={i}) = {knnRange.score(X_test, y_test):.2%}')
