import numpy as np

def load_data():
    x = []
    y_train = []
    f = open('iris.data', 'r')
    dict = {'Iris-versicolor': 1, 'Iris-setosa': 2, 'Iris-virginica': 3}
    for s in f.readlines():
        s_list = s.split(',')[0:len(s)]
        x.append(list(map(float, s_list[:len(s_list) - 1])))  # split input and output and create arrays
        print(s_list[len(s_list) - 1].strip())
        dictk=s_list[len(s_list) - 1].strip()
        if(dictk=='Iris-versicolor'):
            dictk1=float(1)
        elif(dictk=='Iris-setosa'):
            dictk1=float(2)
        elif(dictk=='Iris-virginica'):
            dictk1=float(3)
        y_train.append(dictk1)
    x_train = x
    # np.array(x, dtype=float)
    y_train = np.array(y_train, dtype=float)

    x = []
    y_test = []
    f = open('iris.data', 'r')
    for s in f.readlines():
        s_list = s.split(',')[0:len(s)]
        x.append(list(map(float, s_list[:len(s_list) - 1])))  # split input and output and create arrays
        y_test.append(float(dict[s_list[len(s_list) - 1].strip()]))
        # y_test.append(float(dict[tuple(s_list[len(s_list) - 1].split())]))
    x_test = np.array(x, dtype=float)
    y_test = np.array(y_test, dtype=float)
    return x_train, y_train, x_test, y_test

c = 3 # number of classes
n = 5 # number of parameters


def sigmoid(z):
    return 1.0 / (1 + np.exp(-z))


def train(x, y, alpha, iterations=1000):
    m = y.size
    theta = np.array([0]*n)  # initial values of theta
    i = 0
    while i < iterations:
        updated = np.zeros(n)
        for j in range(n):
            sub = 1 / float(m) * np.sum((sigmoid(theta.T.dot(x.T).T) - y) * x[:, j])
            updated[j] = theta[j] - alpha * sub
        theta = updated
        i += 1
    return theta


xTrain, yTrain, xTest, yTest = load_data()
t_theta = np.array(np.c_[[[0] * n] * c], dtype=float)
xTrain = np.c_[np.ones(xTrain.shape[0]), xTrain]
xTest = np.c_[np.ones(xTest.shape[0]), xTest]

# print xTrain
for i in range(0, c):
    #  update Y for "one against others" strategy
    tmpY=np.copy(yTrain)

    for j in range(len(tmpY)):
        if tmpY[j] == i + 1:
            tmpY[j] = 1
        else:
            tmpY[j] = 0
    t_theta[i] = train(xTrain, tmpY, alpha=0.1)

print ('Values of theta...')
print (t_theta)
test_size = xTest.size


def predict(x, _theta):
    n_class = 3
    res_class = 0
    max_value = -2
    for i in range(n_class):
        theta_i = _theta[i]
        value = sigmoid(theta_i.T.dot(x))
        if value > max_value:
            max_value = value
            res_class = i + 1
    return res_class


for i in range(test_size):
    result = predict(xTest[i], t_theta)
    print('Expected: ', yTest[i], ' Predicted:', result)


import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn import datasets

# import some data to play with
iris = datasets.load_iris()
X = iris.data[:, :2]  # we only take the first two features.
Y = iris.target

logreg = LogisticRegression(C=1e5, solver='lbfgs', multi_class='multinomial')

# Create an instance of Logistic Regression Classifier and fit the data.
logreg.fit(X, Y)

# Plot the decision boundary. For that, we will assign a color to each
# point in the mesh [x_min, x_max]x[y_min, y_max].
x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
h = .02  # step size in the mesh
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
Z = logreg.predict(np.c_[xx.ravel(), yy.ravel()])

# Put the result into a color plot
Z = Z.reshape(xx.shape)
plt.figure(1, figsize=(4, 3))
plt.pcolormesh(xx, yy, Z, cmap=plt.cm.Paired)

# Plot also the training points
plt.scatter(X[:, 0], X[:, 1], c=Y, edgecolors='k', cmap=plt.cm.Paired)
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')

plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.xticks(())
plt.yticks(())

plt.show()