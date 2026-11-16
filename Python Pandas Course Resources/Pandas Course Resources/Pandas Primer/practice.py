import numpy as np
import pandas as pd

sales = [0,5,155,0,518,0,1827,616,317,325]

sales_series = pd.Series(sales, name= "Sales")
# print(sales_series)

'''
Pandas Series have these key properties:
  values  -> the data array in the Series
  index   -> the index array in the Series
  name    -> the optional name for the Series (useful for accessing columns in a DataFrame)
  dtype   -> the data type of the elements in the values array
'''

# print(f'Values: {sales_series.values}')
# print(f'Index: {sales_series.index}')
# print(f'Name: {sales_series.name}')
# print(f'Data Type: {sales_series.dtype}')

'''
The Index
___________________________________________________________
The index lets you easily access "rows" in a Pandas Series or DataFrame
'''
sales = [0,5,155,0,518]
sales_series =pd.Series(sales, name="sales")
# print(sales_series)                         #returns -> # 0      0
                                              # 1      5
                                              # 2    155
                                              # 3      0
                                              # 4    518
                                              # Name: sales, dtype: int64

# print(sales[2])                             # indexing  returns -> 155
# print(sales[2:4])                           # slicing   returns ->  2     155
                                              #                       3     0
                                              #                       Name: sales, dtype: int64

'''
Custom Indices
___________________________________________________________

There are cases where it's applicable to use a custom index for accessing rows
'''

items = ['coffee', 'bananas', 'tea', 'coconut', 'sugar']
sales = [0,5,155,0,518]
sales_series = pd.Series(sales, index=items, name='Sales')
# print(sales_series)
# print(f'The value at sales_series[\'tea\'] is: {sales_series['tea']}')

# print(sales_series['bananas':'coconut'])                    # return -> bananas      5
                                                            #           tea        155
                                                            #           coconut      0
                                                            #           Name: Sales, dtype: int64
                                                            # *code explain*  -> when slicing with custom index makes the 
                                                            #                     stop point "INCLUSIVE"

'''
The iloc Method
_____________________________________________________________
The .iloc[] method is the preferred way to access values by their positional index
  - This method works even when Series have a custom, non-integer index
  - It is more efficient than slicing and is recommended by Pandas' creators

        df.iloc[row position, column position]
         |           |                 |
         V           V                 V
      DataFrame  | The row position  | 
       or Series | 
'''

# items = ['coffee', 'bananas', 'tea', 'coconut', 'sugar']
# sales = [0,5,155,0,518]
# sales_series = pd.Series(sales, index=items, name='Sales')

# print(sales_series.iloc[2])                           # returns ->  155
# print(sales_series.iloc[2:4])                         # returns ->  tea        155
#                                                       #             coconut      0
#                                                       #             Name: Sales, dtype: int64

# print(sales_series.iloc[[1,3,4]])                     # returns ->  bananas      5
#                                                       #             coconut      0
#                                                       #             sugar      518
#                                                       #             Name: Sales, dtype: int64

'''
The loc[] Method
_____________________________________________________________
The .loc[] method is the preferred way to access values by their custom labels

  - This method works even when Series have a custom, non-integer index
  - It is more efficient than slicing and is recommended by Pandas' creators

        df.loc[row position, column position]
         |           |                 |
         V           V                 V
  DataFrame  | The custom row       | 
   or Series | for the values
             | you want 2 access 
             | "pizza" (single row)
             | ['my','pie'](mlty.row)
             | ['jan':'dec'](range) 
'''
# items = ['coffee', 'bananas', 'tea', 'coconut', 'sugar']
# sales = [0,5,155,0,518]
# sales_series = pd.Series(sales, index=items, name='Sales')

# print(sales_series.loc['tea'])                          # returns ->  155
# print(sales_series.loc["bananas":"coconut"])            # returns ->  tea        155
#                                                         #             coconut      0
#                                                         #             Name: Sales, dtype: int64

# print(sales_series.iloc[[1,3,4]])                       # returns ->  bananas      5
#                                                         #             coconut      0
#                                                         #             sugar      518
#                                                         #             Name: Sales, dtype: int64

print(sales_series.reset_index(drop=True))



