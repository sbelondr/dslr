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
from pylib.get_name_column_number import get_name_column_number
from pylib.separate_value import separate_value
from describe import ft_describe
import matplotlib.pyplot as plt
import numpy as np

from pylib.math import *


def calc_std(df, all_X, categs):
    cols = get_name_column_number(df)

    for col in cols:
        if not col == 'Index':
            h1 = np.array(ft_std(all_X[0][col]))
            h2 = ft_std(all_X[1][col])
            h3 = ft_std(all_X[2][col])
            h4 = ft_std(all_X[3][col])

            plt.hist(h1, 50, alpha=0.5, color='r')
            plt.hist(h2, 50, alpha=0.5, color='g')
            plt.hist(h3, 50, alpha=0.5, color='b')
            plt.hist(h4, 50, alpha=0.5, color='y')
            plt.xlabel(col)
            plt.ylabel('std')
            plt.show()

def histogram():
    df = ft_open_csv('ressources/datasets/dataset_train.csv')
    # drop nan value
    df.dropna()
    categs, all_X = separate_value(df, 'Hogwarts House', 6)
    # drop value useless
    # all_X = delete_column(all_X, ['Index', 'Hogwarts House', 'First Name', 'Last Name', 'Birthday', 'Best Hand'])
    clr = ['red', 'blue', 'orange', 'green', 'purple', 'grey']
    i = 0
    calc_std(df, all_X, categs)
    pass

def main():
    histogram();


if __name__ == "__main__":
    main()
