import numpy as np
import pandas as pd

class LogisticRegression(object):
    def __init__(self, alpha=0.01, n_iteration=100):
        self.alpha = alpha
        self.n_iter = n_iteration

    def _scaling(self, X):
        '''
        avoid an overflow
        '''
        for i in range(len(X)):
            X[i] = (X[i] - X.mean())  / X.std()
        return X

    def prepare_X(self, filename, drop):
        data = pd.read_csv(filename, index_col='Index')

        # similaire result (see Histogram)
        del data['Care of Magical Creatures']
        del data['Arithmancy']
        # data identic with defense ag. (see scatter_plot)
        del data['Astronomy']

        X = data.iloc[:,5:]
        X = X.dropna()
        X = np.array(X)
        np.apply_along_axis(self._scaling, 0, X)
        return X

    def prepare_X_Y(self, filename):
        data = pd.read_csv(filename, sep=",", index_col="Index")
        data = data.dropna()

        # similaire result (see Histogram)
        del data['Care of Magical Creatures']
        del data['Arithmancy']
        # data identic with defense ag. (see scatter_plot)
        del data['Astronomy']

        X = np.array((data.iloc[:,5:]))
        y = np.array(data.loc[:, "Hogwarts House"])
        return X, y

    def set_theta(self, theta):
        self.theta = theta

    def _sigmoid_function(self, x):
        value = 1 / (1 + np.exp(-x))
        return value

    def _gradient_descent(self, X, h, theta, y, m):
        gradient_value = np.dot(X.T, (h - y)) / m
        theta -= self.alpha * gradient_value
        return theta

    def fit(self, X, y):
        np.apply_along_axis(self._scaling, 0, X)
        self.theta = []
        X = np.insert(X, 0, 1, axis=1)
        m = len(y)

        for i in np.unique(y):
            y_onevsall = np.where(y == i, 1, 0)
            theta = np.ones(X.shape[1])
            for _ in range(self.n_iter):
                z = X.dot(theta)
                h = y_onevsall - self._sigmoid_function(z)
                gradient = np.dot(X.T, h)
                theta += 5e-5 * gradient
            self.theta.append((theta, i))
        self.theta = np.array(self.theta, dtype=object)
        return self

    def score(self, X, y):
        score = sum(self.predict(X, self.theta) == y) / len(y)
        return score

    def predict(self, X, theta):
        return [ max((i.dot(t), c) for t, c in theta)[1] for i in np.insert(X, 0, 1, axis=1)]
