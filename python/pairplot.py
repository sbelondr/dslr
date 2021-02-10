import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from pylib.ft_open_csv import ft_open_csv
import sys

def pairplot(filename):
    df = ft_open_csv(filename)
    df.dropna()

    del df['Index']
    # similaire result (see Histogram)
    del df['Care of Magical Creatures']
    del df['Arithmancy']
    # data identic with defense ag. (see scatter_plot)
    del df['Astronomy']

    sns.pairplot(df, hue="Hogwarts House", markers = ".")
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) == 2:
        pairplot(sys.argv[1])
    else:
        print("python3 pairplot.py <file.csv>")
