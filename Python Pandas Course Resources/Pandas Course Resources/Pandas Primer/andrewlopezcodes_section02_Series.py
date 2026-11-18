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
# print(oil_series)
# print(f'Mean: {round(oil_series.values.mean(),2)}')
# oil_series.astype("int")
# print(oil_series.astype("int"))
# print(f'Mean: {round(oil_series.values.mean(),2)}')

'''
 Assignment 2:  Accessing Series Data
_______________________________________________________________________
* Set the date series, which has been created below, to be the index of 
the oil price series created in assignment 1.


* Then, take the mean of the first 10 and last 10 prices of the series.


* Finally, grab all oil prices from January 1st, 2017 - January 7th, 2017 
(inclusive) and set the index to the default integer index.
_________________________________________________________________________
'''
# extract date column from oil DataFrame and grab first 100 rows

dates = pd.Series(oil["date"]).iloc[1000:1100]
# print(dates)


oil_series.index = dates
print(oil_series)
print(f'First10 Mean: {round(oil_series.iloc[:10].mean(),2)}')
print(f'Last10 Mean: {round(oil_series.iloc[-10:].mean(),2)}')
print(oil_series.loc["2017-01-01":"2017-01-07"].reset_index(drop=True))