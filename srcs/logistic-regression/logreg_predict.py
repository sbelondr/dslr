# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    logreg_predict.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sbelondr <sbelondr@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/02/16 13:50:58 by sbelondr          #+#    #+#              #
#    Updated: 2021/02/23 11:11:04 by sbelondr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os.path
import sys
import numpy as np
import pandas as pd
from LogisticRegression import LogisticRegression

def ft_check_column_exist(df, column):
    for x in df:
        if x == column:
            return
    print("Column {} not exist".format(column), file = sys.stderr)
    sys.exit(-1)

def prepare_X(filename):
    try:
        data = pd.read_csv(filename, index_col='Index')
    except:
        print('Error during open file', file = sys.stderr)
        sys.exit(-1)

    # similaire result (see Histogram)
    ft_check_column_exist(data, 'Care of Magical Creatures')
    ft_check_column_exist(data, 'Arithmancy')
    ft_check_column_exist(data, 'Astronomy')

    del data['Care of Magical Creatures']
    del data['Arithmancy']
    # data identic with defense ag. (see scatter_plot)
    del data['Astronomy']

    X = data.iloc[:,5:]
    X = np.array(X)
    X = np.nan_to_num(X, nan=1)
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
    if not os.path.isfile('theta.npy'):
        print('File not exist', file = sys.stderr)
        sys.exit(-1)
    theta = np.load('theta.npy', allow_pickle=True)
    X_test = prepare_X(filename)
    predict = LogisticRegression().predict(X_test, theta)
    format_array(predict)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        ft_predict(sys.argv[1])
    else:
        print("python3 logreg_predict.py <file.csv>")
