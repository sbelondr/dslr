# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    logreg_predict.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sbelondr <sbelondr@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/02/10 17:58:07 by sbelondr          #+#    #+#              #
#    Updated: 2021/02/10 18:03:00 by sbelondr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import numpy as np
from LogisticRegression import LogisticRegression
from pylib.ft_open_csv import ft_open_csv

def ft_predict(filename):
    data = np.load('theta.npy', allow_pickle=True)
    logi = LogisticRegression()
    X = logi.prepare_X(filename, False)
    logi.set_theta(data)
    predict = logi.predict(X, data)
    print(predict)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        ft_predict(sys.argv[1])
    else:
        print("python3 logreg_predict.py <file.csv>")
