# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    LogisticRegression.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: samuel <marvin@42.fr>                      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/02/16 13:16:50 by samuel            #+#    #+#              #
#    Updated: 2021/02/16 13:58:32 by sbelondr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from sklearn.utils import shuffle

class LogisticRegression():
    def __init__(self, learning_rate=0.01, n_iteration=100, cost_threshold=0.01):
        self.learning_rate = learning_rate
        self.n_iter = n_iteration
        self.cost_threshold = cost_threshold

    def _scaling(self, X):
        '''
        avoid an overflow
        '''
        for i in range(len(X)):
            X[i] = (X[i] - X.mean()) / X.std()
        return X
    
    def _sigmoid_function(self, x):
        value = 1 / (1 + np.exp(-x))
        return value
    
    def _hypothesis(self, theta, X):
        return 1 / (1 + np.exp(-(np.dot(theta, X.T)))) - 0.0000001
    
    def _compute_cost(self, theta, X, Y):
        reg_strength = 10000
        loss = X.shape[0]
        distances = 1 - Y * (np.dot(X, theta))
        distances[distances < 0] = 0  # max(0, distance)
        hinge_loss = reg_strength * (np.sum(distances) / loss)
        # cost
        cost = 1 / 2 * np.dot(theta, theta) + hinge_loss
        return cost
    
    def _gradient_descent(self, X, h, theta, y, m):
        '''
        theta = theta - alpha * sigma(h^i - y^i)(X^ij)
        '''
        gradient_value = np.dot(X.T, (h - y)) / m
        theta -= self.learning_rate * gradient_value
        return theta

    def _sgd(self, X, y, m):
        dic = dict()

        for i in np.unique(y):
            nth = 0
            prev_cost = float("inf")
            X, y = shuffle(X, y)
            y_onevsall = np.where(y == i, 1, 0)
            theta = np.zeros(X.shape[1])
            dic[i] = list()

            for epoch in range(self.n_iter):
                z = X.dot(theta)
                h = self._sigmoid_function(z)
                theta = self._gradient_descent(X, h, theta, y_onevsall, m)
                dic[i].append(theta)
                if epoch == 2 ** nth or epoch == self.n_iter:
                    cost = self._compute_cost(theta, X, y_onevsall)
                    print("{} -> Epoch is: {} and cost is: {}".format(i, epoch, cost))
                    # stoppage criterion
                    if abs(prev_cost - cost) < self.cost_threshold * prev_cost:
                        break
                    prev_cost = cost
                    nth += 1
            self.theta.append((theta, i))
            self.cost.append((cost, i))
        self.theta_dic = dic
        self.theta = np.array(self.theta, dtype=object)
    
    def fit(self, X, y):
        self.theta = []
        self.cost = []
        np.apply_along_axis(self._scaling, 0, X)
        X = np.insert(X, 0, 1, axis=1)
        m = len(y)
        self._sgd(X, y, m)
        return self
    
    def predict(self, X, thetas):
        np.apply_along_axis(self._scaling, 0, X)
        X = np.insert(X, 0, 1, axis=1)
        X_predicted = [max((self._sigmoid_function(i.dot(theta)), c) for theta, c in thetas)[1] for i in X]
        return X_predicted
    
    def _predict_without_scaling(self, X):
        X = np.insert(X, 0, 1, axis=1)
        X_predicted = [max((self._sigmoid_function(i.dot(theta)), c) for theta, c in self.theta)[1] for i in X]
        return X_predicted
    
    def score(self, X, y):
        score = sum(self._predict_without_scaling(X) == y) / len(y)
        return score
    
    def _plot_cost(self, costh):
        for cost, c in costh:
            plt.plot(range(len(cost)), cost, 'r')
            plt.title('Convergence Graph of Cost Function of type-' + str(c) + ' vs All')
            plt.xlabel('Number of Iterations')
            plt.ylabel('Cost')
            plt.show()

