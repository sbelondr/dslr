# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_linear_regression.py                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sbelondr <sbelondr@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/05/20 14:50:16 by sbelondr          #+#    #+#              #
#    Updated: 2020/05/20 14:52:17 by sbelondr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_linear_regression(x, y):
    '''
    calc linear regression
    Args:
        x: num array
        y: num array
    Return:
        (t0, t1): result theta0 and theta1
    '''
    m = len(x)
    iteration = 10000
    learning_rate = 0.01
    t0 = 0
    t1 = 0
    # nan when keep x
    x_avg = sum(x) / len(x)
    x = x / x_avg
    for it in range(0, iteration):
        predict = t0 + (t1 * x)
        tmp_t0 = (1 / m) * sum(predict - y)
        tmp_t1 = (1 / m) * sum((predict - y) * x)
        t0 = t0 - learning_rate * tmp_t0
        t1 = t1 - learning_rate * tmp_t1
    t1 = t1 / x_avg
    return (t0, t1)