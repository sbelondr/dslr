import numpy as np

def get_name_column_number(df):
    '''
    Returns:
        array with name column contain only number
    '''
    my_lst = list(df)
    cols = []
    for x in my_lst:
        if np.issubdtype(df[x].dtype, np.number):
            cols.append(x)
    return cols
