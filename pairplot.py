import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from pylib.ft_open_csv import ft_open_csv

def pairplot():
    df = ft_open_csv('ressources/datasets/dataset_train.csv')

    del df['Index']
    # similaire result (see Histogram)
    del df['Care of Magical Creatures']
    del df['Arithmancy']
    # data identic with defense ag. (see scatter_plot)
    del df['Astronomy']

    sns.pairplot(df, hue="Hogwarts House", markers = ".")
    plt.show()

if __name__ == "__main__":
    pairplot()