# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: samuel <samuel@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/05/20 19:04:56 by sbelondr          #+#    #+#              #
#    Updated: 2020/05/27 13:52:59 by samuel           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from pylib.ft_open_csv import ft_open_csv
from describe import ft_describe
import matplotlib.pyplot as plt

import numpy as np

def separate_value(df, column, rm_old_column):
    all_categ = df[str(column)]
    all_categ = list(set(all_categ))
    result = []

    for categ in all_categ:
        tmp = df[str(column)] == categ
        data = np.array(df[tmp].iloc[:, rm_old_column:], dtype=float)
        result.append(data)
    return result

def histogram():
    df = ft_open_csv('ressources/datasets/dataset_train.csv')
    # drop nan value
    df.dropna()
    all_X = separate_value(df, 'Hogwarts House', 6)
    # drop value useless
    # all_X = delete_column(all_X, ['Index', 'Hogwarts House', 'First Name', 'Last Name', 'Birthday', 'Best Hand'])
    clr = ['red', 'blue', 'orange', 'green', 'purple', 'grey']
    i = 0

    plt.figure()
    for x in all_X:
        tmp = x
        tmp = tmp[~np.isnan(tmp)]
        plt.hist(tmp, color=clr[i], alpha=0.5)
        i += 1
    #     print(x)
    # h1 = all_X[0]
    # plt.hist(h1, color='red', alpha=0.5)
    plt.show()


    pass

def main():
    histogram();
    # ft_describe('ressources/datasets/dataset_train.csv');


if __name__ == "__main__":
    main()