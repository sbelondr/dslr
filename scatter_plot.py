import numpy as np
import matplotlib.pyplot as plt
from pylib.ft_open_csv import ft_open_csv

def scatter_plot():
    df = ft_open_csv('ressources/datasets/dataset_train.csv')
    # from pylib.get_name_column_number import get_na
    plt.scatter(df['Defense Against the Dark Arts'], df['Astronomy'], c='g')
    plt.xlabel('Defense Against the Dark Arts')
    plt.ylabel('Astronomy')
    plt.show()

if __name__ == "__main__":
	scatter_plot()
