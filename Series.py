import pandas as pd
import math

a = [10, -20, 30, -40]

series = pd.Series(a, index=['a', 'b', 'c', 'd'])
print(series)


def square(x):
    return x ** 2


def module_seruoes(x):
    return int(math.fabs(x))


square_series = series.apply(module_seruoes)
print(square_series)