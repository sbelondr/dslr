import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from pylib.ft_open_csv import ft_open_csv
from pylib.ft_check_column_exist import ft_check_column_exist
import sys

def pairplot(filename):
    df = ft_open_csv(filename)
    df.dropna()

    ft_check_column_exist(df, 'Index')
    ft_check_column_exist(df, 'Care of Magical Creatures')
    ft_check_column_exist(df, 'Arithmancy')
    ft_check_column_exist(df, 'Astronomy')
    ft_check_column_exist(df, 'Hogwarts House')
    del df['Index']
    # similaire result (see Histogram)
    del df['Care of Magical Creatures']
    del df['Arithmancy']
    # data identic with defense ag. (see scatter_plot)
    del df['Astronomy']

    try:
        sns.pairplot(df, hue="Hogwarts House", palette=dict(Ravenclaw = "Blue", Slytherin = "Green", Hufflepuff = "Yellow", Gryffindor = "Red"),markers = ".")
        plt.show()
    except:
        print('An exception occurred', file = sys.stderr)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        pairplot(sys.argv[1])
    else:
        print("python3 pairplot.py <file.csv>")
        sys.exit(1)
