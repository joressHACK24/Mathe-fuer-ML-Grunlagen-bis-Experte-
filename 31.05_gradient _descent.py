'''import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

X = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])




def batch_gradient_descent(X, y, learning_rate, epochs):

    w = 0
    b = 0
    w_rep = []
    b_rep = []
    J_rep = []
    plt.figure(figsize=(6, 5))
    for i in range(epochs):
        y_pred = w * X + b

        w -= learning_rate * (1/(X.shape[0]))*np.sum((y_pred- y)*X)
        b -= learning_rate * (1/(X.shape[0]))*np.sum((y_pred- y))
        J = (1/2*X.shape[0]) * np.sum((y_pred-y)**2)
        w_rep.append(w)
        b_rep.append(b)
        J_rep.append(J)
        
    print(w, b)
    print(J_rep)
    
    
    axes = plt.axes(projection="3d")
    axes.scatter3D(w_rep, b_rep, J_rep)
    plt.plot(X,y)
    
    plt.show()

batch_gradient_descent(X,y,0.01,1000)'''

#_______________________________________________________________________________________________________________________

import numpy as np

# X = [Surface (m2), Nombre de chambres]
X = np.array([
    [50, 1],
    [80, 2],
    [120, 3],
    [150, 3],
    [200, 4]
])

# y = Prix (en milliers d'euros)
y = np.array([150, 250, 350, 420, 600])

w = np.zeros(X.shape[1])
b = 0

m = len(X)
epochs = 100
learning_rate = 0.01


def standardisation(X):
    x_neu = np.array([[]])
    for i in range(m):
        
        u = np.mean(X)
        o = np.std(X)
        x_neu = (X - u)/o
    return x_neu

X_neu = standardisation(X)
print(X_neu)
for i in range(epochs):
    y_pred = X_neu @ w + b

    w -= learning_rate * (1/m) * (mplement multivariate gradient descent with Z-score(X_neu.T) @(y_pred - y))
    b -= learning_rate * (1/m) * np.sum((y_pred - y))


print(w)
print(b)