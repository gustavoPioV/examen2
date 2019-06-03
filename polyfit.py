import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def polyfit(x, y, n):
    xlen = len(x)
    ylen = len(y)
    one = np.ones((xlen, n + 1), dtype = int)
    #print(one)
    xT = np.matrix(x)
    yT = np.matrix(y)
    c2 = np.power(xT, 2)
    c3 = np.power(xT, 3)
    print(xT)
    c1 = one[:, [1]]
    #print(c1)
    A = np.hstack([c1, xT, c2, c3])
    #print(A)

    def inv(A):
        return np.linalg.inv(A)

    def trans(A):
        return A.getT()

    def prod(A,B):
        return np.dot(A,B)

    AtA = inv(prod(trans(A), A))
    #print(AtA)

    up = prod(AtA, trans(A))

    u = prod(up, trans(yT))
    print(u)

dataset = pd.read_csv('exam_B_dataset.csv')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values
polyfit(x, y, 4)
plt.scatter(x, y)
plt.plot(x, polyfit)
plt.show()

