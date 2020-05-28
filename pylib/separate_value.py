def separate_value(df, column, rm_old_column):
    all_categ = df[str(column)]
    all_categ = list(set(all_categ))
    result = []

    for categ in all_categ:
        tmp = df[str(column)] == categ
        data = df[tmp]
        result.append(data)
    return all_categ, result
