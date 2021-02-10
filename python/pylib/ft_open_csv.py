# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_open_csv.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sbelondr <sbelondr@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/05/20 14:54:02 by sbelondr          #+#    #+#              #
#    Updated: 2021/02/10 17:13:19 by sbelondr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd
import sys

def ft_open_csv(filename):
    '''
    Open csv and return dataframe
    Args:
        filename: file name
    Return:
        dataframe
    '''
    if filename == "":
        print("You didn't give a file")
        sys.exit(-1)
    try:
        df = pd.read_csv(str(filename))
    except IOError:
        print("File error")
        sys.exit(-1)
    return df
