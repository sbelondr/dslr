# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_read_file.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sbelondr <sbelondr@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/05/20 15:00:34 by sbelondr          #+#    #+#              #
#    Updated: 2020/05/20 15:01:29 by sbelondr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_read_file(filename):
    try:
        f = open(filename, "r")
        s = f.read().split()
    except IOError:
        s = ""
    return s