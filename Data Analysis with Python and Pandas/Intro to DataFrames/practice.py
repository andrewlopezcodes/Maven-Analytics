import pandas as pd
import numpy as np

'''
Creating DataFrame
___________________________________________________________________
DataFrames are Pandas “tables” made up from columns and rows
  - Each column of data in a DataFrame is a Pandas Series that shares the same row index
  - The column headers work as a column index that contains the Series names

          
              -----  id  date        store_nbr   <-  axis = 1
              |   0   0   2013-01-01    1
              |   1   1   2013-01-01    1
 axis = 0 ----|   2   2   2013-01-01    1
              |   3   3   2013-01-01    1
              |   4   4   2013-01-01    1
              -----

DataFrames have these key properties:
  - shape   > the number of rows and columns in a DataFrame (the index is not considered a column)
  - index   > the row index in a DataFrame, by default a range of integers (axis= 0)
  - columns > the column index in a DataFrame, represented by the Series names (axis= 1)
  - axes    > the row and column indices in a DataFrame
  - dtypes  > the data type for each Series in a DataFrame (they can b different!)

  print(df.shape)   returns ->  (3000888, 6)
  print(df.index)   returns ->  RangeIndex(start= 0, stop=3000888, step=1)
  print(df.columns) returns ->  ['id', 'date', 'stor_nbr', 'family', 'sales', 'on_promotion']
  print(df.axes)    returns ->  [RangeIndex(start= 0, stop=3000888, step=1),
                                  Index(['id', 'date', 'stor_nbr', 'family', 'sales', 'on_promotion'])
                                ]
  print(df.dtypes)  returns ->  id           int64
                                store_nbr    int64
                                family         str
                                dtype: object



You can create a DataFrame from a Python dictionary or NumPy array by using the 
Pandas DataFrame() function

  pd.DataFrame(
    { "id": [1,2],
      "store_nbr": [1, 2],
      "family": ["POULTRY", "PRODUCE"]
    }
  )                                       returns ->     id  store_nbr   family
                                                      0   1          1  POULTRY
                                                      1   2          2  PRODUCE

Creating A DataFrame
___________________________________________________________________
You'll more likely create a DataFrame by using the Pandas read_csv() 
function. You'll usually read in a flat file (csv, txt, or tsv)

  import pandas as pd
  oil = pd.read_csv('oil.csv')
  print(oil)                            returns ->              date  dcoilwtico
                                                    0     2013-01-01         NaN
                                                    1     2013-01-02       93.14
                                                    2     2013-01-03       92.97
                                                    3     2013-01-04       93.12
                                                    4     2013-01-07       93.20
                                                    ...          ...         ...
                                                    1213  2017-08-25       47.65
                                                    1214  2017-08-28       46.40
                                                    1215  2017-08-29       46.46
                                                    1216  2017-08-30       45.96
                                                    1217  2017-08-31       47.26
                                                    [1218 rows x 2 columns]       <-  *code explain*  shape of the dataFrame
                                                                                                      print(oil.shape)

___________________________________________________________________
'''
# homeDF = pd.DataFrame(
#     { "id": [1,2],
#       "store_nbr": [1, 2],
#       "family": ["POULTRY", "PRODUCE"]
#     }
# )

# print(homeDF.shape)       #returns  ->  (2, 3)
# print(homeDF.index)       #returns  ->  RangeIndex(start=0, stop=2, step=1)
# print(homeDF.columns)     #returns  ->  Index(['id', 'store_nbr', 'family'], dtype='str')
# print(homeDF.axes)        #returns  ->  [RangeIndex(start=0, stop=2, step=1), Index(['id', 'store_nbr', 'family'], dtype='str')]
# print(homeDF.dtypes)


oil = pd.read_csv('oil.csv')
print(oil)
print(oil.shape)
print(oil.index)
print(oil.columns)
oil.columns = ['price_date', 'oil_price']
print(oil.axes)
print(oil.dtypes)
print(oil)