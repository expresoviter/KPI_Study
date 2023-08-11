from sklearn.svm import SVC
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(1)
xXor = np.random.randn(200, 2)
yXor = np.logical_xor(xXor[:, 0] > 0, xXor[:, 1] > 0)
yXor = np.where(yXor, 1, -1)
plt.scatter(xXor[yXor == 1, 0], xXor[yXor == 1, 1], c='b', marker='x', label='1')
plt.scatter(xXor[yXor == -1, 0], xXor[yXor == -1, 1], c='r', marker='s', label='-1')
plt.xlim([-3, 3])
plt.ylim([-3, 3])
plt.legend(loc='best')
plt.show()


def plotDecisionRegions(x, y, classifier, test_idx=None, resolution=0.02):
    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])

    x1Min, x1Max = x[:, 0].min() - 1, x[:, 0].max() + 1
    x2Min, x2Max = x[:, 1].min() - 1, x[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1Min, x1Max, resolution), np.arange(x2Min, x2Max, resolution))
    z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    z = z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, z, alpha=0.3, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())

    for idx, c1 in enumerate(np.unique(y)):
        plt.scatter(x=x[y == c1, 0], y=x[y == c1, 1], alpha=0.8, c=colors[idx], marker=markers[idx], label=c1,
                    edgecolor='black')
    if test_idx:
        xTest, yTest = x[test_idx, :], y[test_idx]
        plt.scatter(xTest[:, 0],
                    xTest[:, 1],
                    c="black",
                    edgecolor='black',
                    alpha=1.0,
                    linewidth=1,
                    marker='o',
                    s=100,
                    label='Zestaw testowy')


svm = SVC(kernel='rbf', random_state=1, gamma=0.10, C=10.0)
svm.fit(xXor, yXor)
plotDecisionRegions(xXor, yXor, classifier=svm)
plt.legend(loc='upper left')
plt.show()
