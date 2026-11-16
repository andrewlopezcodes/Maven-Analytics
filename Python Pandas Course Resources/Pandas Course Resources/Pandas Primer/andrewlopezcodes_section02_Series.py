'''
 Assignment 1: Series Basics
_________________________________________________________________
The code has been previded to create an array, `oil_array` from a 
dataframe column. 

* Convert `oil_array` into a Pandas Series, called `oil_series`. 
  Give it a name!
* Return the name, dtype, size, and index of `oil_series`.

Take the mean of the values array. 

Then, convert the series to integer datatype and recalculate the 
mean. 
__________________________________________________________________
'''
import numpy as np
import pandas as pd
# create a DataFrame from the oil file, drop missing values
oil = pd.read_csv("C:\\Users\\sneak\\Desktop\\Maven Analytics\\Python Pandas Course Resources\\Pandas Course Resources\\Pandas Primer\\oil.csv").dropna()

# Grab 100 rows of oil prices
oil_array = np.array(oil["dcoilwtico"].iloc[1000:1100])

# print(oil_array)

oil_series = pd.Series(oil_array, name="oil_prices")
print(oil_series)
print(f'Mean: {round(oil_series.values.mean(),2)}')
oil_series.astype("int")
print(oil_series.astype("int"))
print(f'Mean: {round(oil_series.values.mean(),2)}')
