# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    logreg_train.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sbelondr <sbelondr@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/02/10 17:51:17 by sbelondr          #+#    #+#              #
#    Updated: 2021/02/10 17:56:21 by sbelondr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import numpy as np
from LogisticRegression import LogisticRegression

def ft_train(filename):
    X, y = LogisticRegression().prepare_X_Y(filename)
    logi = LogisticRegression(n_iteration=30000).fit(X, y)

    print(logi.theta)
    np.save('theta', logi.theta)
    print(logi.score(X, y))

if __name__ == "__main__":
    if len(sys.argv) == 2:
        ft_train(sys.argv[1])
    else:
        print("python3 logreg_train.py <file.csv>")
