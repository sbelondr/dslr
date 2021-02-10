# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_open_csv.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sbelondr <sbelondr@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/05/20 14:54:02 by sbelondr          #+#    #+#              #
#    Updated: 2020/05/20 17:27:58 by sbelondr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd

def ft_open_csv(filename):
    '''
    Open csv and return dataframe
    Args:
        filename: file name
    Return:
        dataframe
    '''
    try:
        df = pd.read_csv(str(filename))
    except IOError:
        print("File error")
        return -1
    # X = df.iloc[0:len(df),0]
    # Y = df.iloc[0:len(df),1]
    return df