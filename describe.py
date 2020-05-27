import sys;
from pylib.ft_open_csv import ft_open_csv
import numpy as np;
from pylib.math import *


def add_space(src, nb):
    sz = len(src)
    calc = nb - sz
    result = ''
    while (calc > 0):
        result += ' '
        calc -= 1
    return result

def display_line(name_line, line, wh_col, start):
    result = ''
    if start:
        result = '          '
    else:
        result = name_line + add_space(name_line, 10)
    i = 0
    for x in line:
        result += str(x)
        result += add_space(str(x), wh_col[i] + 5)
        i += 1
    print(result)

def display_describe(l_name, l_cnt, l_mean, l_std, l_min, l_25, l_50, l_75, l_max, l_sz_column):
    display_line('', l_name, l_sz_column, 1)
    display_line('Count', l_cnt, l_sz_column, 0)
    display_line('Mean', l_mean, l_sz_column, 0)
    display_line('Std', l_std, l_sz_column, 0)
    display_line('Min', l_min, l_sz_column, 0)
    display_line('25%', l_25, l_sz_column, 0)
    display_line('50%', l_50, l_sz_column, 0)
    display_line('75%', l_75, l_sz_column, 0)
    display_line('Max', l_max, l_sz_column, 0)
    pass



def ft_size_column(line, i, max_col):
    value = len(str(line[i]))
    if (value > max_col):
        max_col = value
    return max_col


def ft_describe(argv):
    df = ft_open_csv('ressources/datasets/dataset_train.csv')
    my_lst = list(df);
    line_name = [];
    line_count = [];
    line_mean = [];
    line_std = [];
    line_min = [];
    line_25 = [];
    line_50 = [];
    line_75 = [];
    line_max = [];
    line_sz_column = [];

    for x in my_lst:
        if np.issubdtype(df[x].dtype, np.number):
            line_name.append(x)
            line_sz_column.append(len(x))
    # fill all array
    i = 0
    for x in line_name:
        # line_sz_column.append(0)
        line_count.append(ft_count(df[x]))
        line_sz_column[i] = ft_size_column(line_count, i, line_sz_column[i])
        line_mean.append(ft_mean(df[x]));
        line_sz_column[i] = ft_size_column(line_mean, i, line_sz_column[i])
        line_std.append(ft_std(df[x]));
        line_sz_column[i] = ft_size_column(line_std, i, line_sz_column[i])
        line_min.append(ft_min(df[x]));
        line_sz_column[i] = ft_size_column(line_min, i, line_sz_column[i])
        line_25.append(ft_percentile(df[x], 25));
        line_sz_column[i] = ft_size_column(line_25, i, line_sz_column[i])
        line_50.append(ft_percentile(df[x], 50));
        line_sz_column[i] = ft_size_column(line_50, i, line_sz_column[i])
        line_75.append(ft_percentile(df[x], 75));
        line_sz_column[i] = ft_size_column(line_75, i, line_sz_column[i])
        line_max.append(ft_max(df[x]));
        line_sz_column[i] = ft_size_column(line_max, i, line_sz_column[i])
        i += 1;

    display_describe(line_name, line_count, line_mean, line_std, line_min, line_25, line_50, line_75, line_max, line_sz_column)

if __name__ == "__main__":
    ft_describe(sys.argv[0])
