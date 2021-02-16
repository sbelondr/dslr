# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    sgd.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sbelondr <sbelondr@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/02/16 13:27:09 by sbelondr          #+#    #+#              #
#    Updated: 2021/02/16 13:55:11 by sbelondr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import numpy as np
import pandas as pd
from LogisticRegression import LogisticRegression

def prepare_X_Y(filename):
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

def ft_train(filename):
    # train
    X, y = prepare_X_Y(filename)
    logi = LogisticRegression(learning_rate=0.01, n_iteration=300000, cost_threshold=0.01).fit(X, y)
    print("\nScore is: {}.".format(logi.score(X, y)))
    np.save('theta', logi.theta)
    return logi

if __name__ == "__main__":
    if len(sys.argv) == 2:
        ft_train(sys.argv[1])
    else:
        print("python3 logreg_train.py <file.csv>")
