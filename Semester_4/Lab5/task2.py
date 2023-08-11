from keras.datasets import cifar10
from keras import models
from keras.layers import Dense, Flatten, Conv2D
from keras.utils import to_categorical
import matplotlib.pyplot as plt


def train(train_images, train_labels, test_images, test_labels):
    print('train_images shape:', train_images.shape)
    print('train_labels shape:', train_labels.shape)

    plt.figure(figsize=(10, 10))
    for i in range(25):
        plt.subplot(5, 5, i + 1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(train_images[i], cmap=plt.cm.binary)
        plt.xlabel(labels[train_labels[i][0]])
    plt.show()

    train_images = train_images.astype('float32')
    test_images = test_images.astype('float32')
    train_images /= 255
    test_images /= 255

    train_labels = to_categorical(train_labels)
    test_labels = to_categorical(test_labels)

    model = models.Sequential()

    model.add(Conv2D(32, (3, 3), padding='same', activation="relu", input_shape=train_images.shape[1:]))
    model.add(Flatten())
    model.add(Dense(512, activation='relu'))
    model.add(Dense(512, activation='relu'))

    model.add(Dense(10, activation='softmax'))

    model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
    model.fit(train_images, train_labels, epochs=5, batch_size=128)
    test_loss, test_acc = model.evaluate(test_images, test_labels)
    model.save("model2.h5")


def test(test_images, test_labels, no):
    model = models.load_model('model2.h5')
    fig = plt.figure(figsize=(3, 3))
    test_image = test_images[no]
    test_result = list(model.predict(test_image.reshape((1, 32, 32, 3)))[0])
    plt.imshow(test_image)
    dict_key = test_result.index(max(test_result))
    plt.title("Predicted: {} \nTrue Label: {}".format(labels[dict_key], labels[test_labels[no][0]]))
    plt.show()


if __name__ == "__main__":
    (train_images, train_labels), (test_images, test_labels) = cifar10.load_data()
    labels = ['Airplane', 'Automobile', 'Bird', 'Cat', 'Deer', 'Dog', 'Frog', 'Horse', 'Ship', 'Truck']
    #train(train_images, train_labels, test_images, test_labels)
    for i in range(203, 206):
        test(test_images, test_labels, i)
