import sys
import numpy as np
import matplotlib.pyplot as plt
from pylib.ft_open_csv import ft_open_csv
from pylib.ft_check_column_exist import ft_check_column_exist

def scatter_plot(filename):
    df = ft_open_csv(filename)
    ft_check_column_exist(df, 'Defense Against the Dark Arts')
    ft_check_column_exist(df, 'Astronomy')
    plt.scatter(df['Defense Against the Dark Arts'], df['Astronomy'], c='g')
    plt.xlabel('Defense Against the Dark Arts')
    plt.ylabel('Astronomy')
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) == 2:
        scatter_plot(sys.argv[1])
    else:
        print("python3 scatter_plot.py <file.csv>")
        sys.exit(1)
