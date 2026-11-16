import numpy as np
import pandas as pd

sales = [0,5,155,0,518,0,1827,616,317,325]

sales_series = pd.Series(sales, name= "Sales")
print(sales_series)

'''
Pandas Series have these key properties:
  values  -> the data array in the Series
  index   -> the index array in the Series
  name    -> the optional name for the Series (useful for accessing columns in a DataFrame)
  dtype   -> the data type of the elements in the values array
'''

print(f'Values: {sales_series.values}')
print(f'Index: {sales_series.index}')
print(f'Name: {sales_series.name}')
print(f'Data Type: {sales_series.dtype}')