import numpy as np
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

batch_gradient_descent(X,y,0.01,1000)


