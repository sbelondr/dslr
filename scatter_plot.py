import matplotlib.pyplot as plt
from pylib.ft_open_csv import ft_open_csv
# from pylib.get_name_column_number import get_name_column_number

def scatter_plot():
	df = ft_open_csv('ressources/datasets/dataset_train.csv')
	df.dropna()

	plt.scatter(df['Defense Against the Dark Arts'], df['Astronomy'], c='g')
	plt.xlabel('Defense Against the Dark Arts')
	plt.ylabel('Astronomy')
	plt.show()

	# cols = get_name_column_number(df)
	# for col in cols:
	#     if not col == 'Index':
	#         for x in cols:
	#             if x != 'Index' and x != col:
	#                 plt.scatter(df[col], df[x], c='g')
	#                 plt.xlabel(col)
	#                 plt.ylabel(x)
	#                 plt.show()

if __name__ == "__main__":
	scatter_plot()
