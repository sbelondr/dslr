import numpy as np

def gradientDescent(X, y, theta, alpha, num_iters):
    '''
       Performs gradient descent to learn theta
       theta = np.ones(X.shapes[1]), alpha = 0.01, num_iters = 300000
    '''
    m = y.size  # number of training examples
    for i in range(num_iters):
        y_hat = np.dot(X, theta)
        theta = theta - alpha * (1.0/m) * np.dot(X.T, y_hat-y)
    return theta