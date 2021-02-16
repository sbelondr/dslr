# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    logreg_predict.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sbelondr <sbelondr@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/02/16 13:50:58 by sbelondr          #+#    #+#              #
#    Updated: 2021/02/16 14:26:25 by sbelondr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import numpy as np
import pandas as pd
from LogisticRegression import LogisticRegression

def prepare_X(filename):
    data = pd.read_csv(filename, index_col='Index')
    # similaire result (see Histogram)
    del data['Care of Magical Creatures']
    del data['Arithmancy']
    # data identic with defense ag. (see scatter_plot)
    del data['Astronomy']

    X = data.iloc[:,5:]
    X = X.dropna()
    X = np.array(X)
    return X

def format_array(arr):
    form = list()
    form.append("Index,Hogwarts House\n")
    for i, x in enumerate(arr, start=0):
        form.append(str(i) + ',' + x + '\n')
    with open('houses.csv', 'w') as f:
        for x in form:
            f.write(x)
        f.close()

def ft_predict(filename):
    theta = np.load('theta.npy', allow_pickle=True)
    X_test = prepare_X(filename)
    predict = LogisticRegression().predict(X_test, theta)
    format_array(predict)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        ft_predict(sys.argv[1])
    else:
        print("python3 logreg_predict.py <file.csv>")
