# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_check_column_exist.py                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sbelondr <sbelondr@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/02/17 14:09:24 by sbelondr          #+#    #+#              #
#    Updated: 2021/02/17 14:21:04 by sbelondr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def ft_check_column_exist(df, column):
    for x in df:
        if x == column:
            return
    print("Column {} not exist".format(column), file = sys.stderr)
    sys.exit(-1)
