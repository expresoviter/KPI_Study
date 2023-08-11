import pandas as pd
from keras import models
from keras.utils import to_categorical
from keras.layers import Dense, Flatten


def transform(path):
    df = pd.read_csv(path, index_col=0)
    print(df)

    data = df.values
    X_train, y_train = data[:, :-1], data[:, -1]
    y_train = to_categorical(y_train)

    for i in range(len(X_train)):
        for j in range(4):
            X_train[i][j] /= 200
    return X_train, y_train


def modell(X_train, y_train):
    model = models.Sequential()
    model.add(Flatten())
    model.add(Dense(512, activation='relu'))
    model.add(Dense(2, activation='softmax'))

    model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])
    model.fit(X_train, y_train, epochs=15, batch_size=32)
    model.save("model.h5")


def test(path):
    model = models.load_model('model.h5')
    df = pd.read_csv(path, index_col=0)

    data = df.values
    X, y = data[:, :-1], data[:, -1]
    y = to_categorical(y)

    for i in range(len(X)):
        for j in range(4):
            X[i][j] /= 200

    test_loss, test_acc = model.evaluate(X, y)
    prediction = list(model.predict(X))
    prediction = [list(prediction[i]).index(max(list(prediction[i]))) for i in range(len(prediction))]
    predictedDf = []
    predictedNot = []
    for i in range(len(prediction)):
        if prediction[i] == y[i][0]:
            predictedDf.append(list(X[i]))
        else:
            predictedNot.append(list(X[i]))
            predictedNot[-1].append(df.iloc[i, 5])
    predictedDf = pd.DataFrame(predictedDf)
    predictedNot = pd.DataFrame(predictedNot)

    predictedDf.columns = ["math", "ukr", "eng", "rating", "benefit"]
    predictedNot.columns = ["math", "ukr", "eng", "rating", "benefit", "actual"]
    for i in ["math", "ukr", "eng", "rating"]:
        predictedDf[i] *= 200
        predictedNot[i] *= 200
    predictedDf = predictedDf.sort_values(by=["benefit", "rating"], ascending=False)
    predictedNot = predictedNot.sort_values(by=["benefit", "rating"], ascending=False)
    predictedDf.to_excel(str(path.split('.')[0] + ".xlsx"))
    predictedNot.to_excel(str(path.split('.')[0] + "Not.xlsx"))


if __name__ == "__main__":
    # x, y = transform("data0.csv")
    # modell(x, y)
    test("data1.csv")
    test("data2.csv")
    test("data3.csv")
