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
# print(oil)
# print(oil.shape)
# print(oil.index)
# print(oil.columns)
oil.columns = ['price_date', 'oil_price']
# print(oil.axes)
# print(oil.dtypes)
# print(oil)

'''
EXPLORING A DATAFRAME
___________________________________________________________________
You can explore a DataFrame with these Pandas methods

Method                      Descriptions                      
====================================================================
head      df.head(nrows)        Returns the first n rows of the DataFrame (5 by default) 
tail      df.tail(nrows)        Returns the last n rows of the DataFrame (5 by default) 
sample    df.sample(n)rows      Returns n rows from a random sample (1 by default) 
info      df.info()             Returns key details on a DataFrame size , columns, and memory usage 
describe  df.describe(include)  Returns descriptive statistics for the columns in a DataFrame (only numeric
                                columns by default; use the "include" argument to specify more columns) 

====================================================================
 HEAD & TAIL 
====================================================================                             
The .head() and .tail()methods return the top or bottom rows in a DataFrame
• This is a great way to QA data upon import!
• You can change the number of rows by entering an integer

print(df.head(20))
print(dr.tail(6))


====================================================================
 SAMPLE 
==================================================================== 
The .sample() method returns a random sample of rows from a DataFrame
  - The .sample() method returns 1 row by default
  - You can specify the number of rows to return, in this case 38, and 
    set a random_state to ensure your sample can be reproduced later 
    if needed.

print(df.sample(38, random_state=12345))


====================================================================
 INFO
==================================================================== 
The .info() method returns details on a DataFrame properties and memory usage

  - The .info() method will show non-null counts
    on a DataFrame with less than ~1.7m rows,
    but you can specify show_counts=True to
    ensure they are always displayed
    This is a great way to quickly identify missing
    values 

  – if the non-null count is less than the
    total number of rows, then the difference is
    the number of NaN values in that column!
    (In this case there are none)

print(oil.info())                     returns ->  RangeIndex: 1218 entries, 0 to 1217
                                                  Data columns (total 2 columns):
                                                      Column      Non-Null Count  Dtype
                                                    ---  ------      --------------  -----
                                                      0   price_date  1218 non-null   str    
                                                      1   oil_price   1175 non-null   float64
                                                      dtypes: float64(1), str(1)
                                                      memory usage: 19.2 KB
                                                      None


print(oil.info(show_counts=True))     returns ->  <class 'pandas.DataFrame'>
                                                  RangeIndex: 1218 entries, 0 to 1217
                                                  Data columns (total 2 columns):
                                                  #   Column      Non-Null Count  Dtype  
                                                  ---  ------      --------------  -----  
                                                   0   price_date  1218 non-null   str    
                                                   1   oil_price   1175 non-null   float64
                                                   dtypes: float64(1), str(1)
                                                   memory usage: 19.2 KB
                                                   None
====================================================================
 DESCRIBE
==================================================================== 
The .describe() method returns key statistics on DataFrame columns

  - Use include=“all” to return statistics for all columns, or choose 
    a specific data type to include
  - Note that the .round() method suppresses scientific notation and
    makes the output more readable
  

  print(oil.describe())                   returns ->           oil_price
                                                      count  1175.000000
                                                      mean     67.714366
                                                      std      25.630476
                                                      min      26.190000
                                                      25%      46.405000
                                                      50%      53.190000
                                                      75%      95.660000
                                                      max     110.620000



  print(oil.describe(include="all"))      returns ->          price_date    oil_price
                                                      count         1218  1175.000000
                                                      unique        1218          NaN ->  Unique values
                                                      top     2013-01-01          NaN ->  most common value (top)
                                                      freq             1          NaN ->  its frequency being 1 means the dates don't repeat
                                                      mean           NaN    67.714366
                                                      std            NaN    25.630476
                                                      min            NaN    26.190000
                                                      25%            NaN    46.405000
                                                      50%            NaN    53.190000
                                                      75%            NaN    95.660000
                                                      max            NaN   110.620000


print(oil.describe(include="all").round())      returns ->          price_date  oil_price
                                                            count         1218     1175.0
                                                            unique        1218        NaN
                                                            top     2013-01-01        NaN
                                                            freq             1        NaN
                                                            mean           NaN       68.0
                                                            std            NaN       26.0
                                                            min            NaN       26.0
                                                            25%            NaN       46.0
                                                            50%            NaN       53.0
                                                            75%            NaN       96.0
                                                            max            NaN      111.0

___________________________________________________________________
'''

# print(oil.info())
# print(oil.info(show_counts=True)) 
# print(oil.describe(include="all").round())


'''
  ACCESSING DATAFRAME COLUMNS
___________________________________________________________________
You can access a DataFrame column by using bracket or dot notation
  - Dot notation only works for valid Python variable names 
    (no spaces, special characters, etc.), and if the column name is 
    not the same as an existing variable or method

  - PRO TIP: Even though you will see many examples of dot notation 
    in use, stick to bracket notation for single columns of data 
    as it is less likely to cause issues  


  - You can use Series operations on DataFrame columns (each column is a Pandas Series!)


  - 


  print(oil['price_date'])                    returns ->  0       2013-01-01
                                                          1       2013-01-02
                                                          2       2013-01-03
                                                          3       2013-01-04
                                                          4       2013-01-07
                                                                     ...    
                                                          1213    2017-08-25
                                                          1214    2017-08-28
                                                          1215    2017-08-29
                                                          1216    2017-08-30
                                                          1217    2017-08-31
                                                          Name: price_date, Length: 1218, dtype: str


print(oil.price_date)                         returns ->  0       2013-01-01
                                                          1       2013-01-02
                                                          2       2013-01-03
                                                          3       2013-01-04
                                                          4       2013-01-07
                                                                     ...    
                                                          1213    2017-08-25
                                                          1214    2017-08-28
                                                          1215    2017-08-29
                                                          1216    2017-08-30
                                                          1217    2017-08-31
                                                          Name: price_date, Length: 1218, dtype: str


print(oil['oil_price'].nunique())                         returns ->  998
print(oil['oil_price'].mean().round())                    returns ->  68.0
print(oil['oil_price'].sum().round())                     returns ->  79564.0
print(oil['oil_price'].value_counts().iloc[:5])           returns ->   oil_price          *code explain*  ->  This code finds the top 5 most 
                                                                      93.12    4                              common oil prices in your data 
                                                                      96.44    4                              and counts how many times each 
                                                                      60.01    4                              one appears.
                                                                      47.65    4
                                                                      47.72    4
                                                                      Name: count, dtype: int64


You can select multiple columns with a list of column names between brackets
  - This is ideal for selecting non-consecutive columns in a DataFrame

  print(oil[['oil_price','price_date']].fillna(0))            returns ->          oil_price  price_date
                                                                            0          0.00  2013-01-01
                                                                            1         93.14  2013-01-02
                                                                            2         92.97  2013-01-03
                                                                            3         93.12  2013-01-04
                                                                            4         93.20  2013-01-07
                                                                            ...         ...         ...
                                                                            1213      47.65  2017-08-25
                                                                            1214      46.40  2017-08-28
                                                                            1215      46.46  2017-08-29
                                                                            1216      45.96  2017-08-30
                                                                            1217      47.26  2017-08-31
                                                                            [1218 rows x 2 columns]

column bracket notation should primarily be used for creating new columns and quick exploration

oil.columns = ['date','price']                      *code explain*  ->  changing the name of the columns

print(oil)                                          returns =>              date  price
                                                                0     2013-01-01    NaN
                                                                1     2013-01-02  93.14
                                                                2     2013-01-03  92.97
                                                                3     2013-01-04  93.12
                                                                4     2013-01-07  93.20
                                                                ...          ...    ...
                                                                1213  2017-08-25  47.65
                                                                1214  2017-08-28  46.40
                                                                1215  2017-08-29  46.46
                                                                1216  2017-08-30  45.96
                                                                1217  2017-08-31  47.26
                                                                [1218 rows x 2 columns]

print(oil[['price','date']])                        returns =>          price        date
                                                                  0       NaN  2013-01-01
                                                                  1     93.14  2013-01-02
                                                                  2     92.97  2013-01-03
                                                                  3     93.12  2013-01-04
                                                                  4     93.20  2013-01-07
                                                                  ...     ...         ...
                                                                  1213  47.65  2017-08-25
                                                                  1214  46.40  2017-08-28
                                                                  1215  46.46  2017-08-29
                                                                  1216  45.96  2017-08-30
                                                                  1217  47.26  2017-08-31
                                                                  [1218 rows x 2 columns]




___________________________________________________________________
'''

# print(oil['price_date'])
# print(oil.price_date)
# print(oil['oil_price'].nunique())
# print(f'This is the average: ${oil['oil_price'].mean().round()}')
# print(f'This is the sum of oil prices: ${oil['oil_price'].sum().round()}')
# print(f'This is the first 5 unique values in a column with their frequencies:\n {oil['oil_price'].value_counts().iloc[:5]}')
# print(oil[['oil_price','price_date']].fillna(0))
oil.columns = ['date','price']
# print(oil)
# print(oil[['price','date']])


'''
ACCESSING DATA WITH ILOC
___________________________________________________________________
The .iloc() accessor filters DataFrames by their row and column indices
• The first parameter accesses rows, and the second accesses columns

print(oil.iloc[:5,:])     returns ->           date  price    *code explain*  ->  ".iloc[:5,:]" return index, start with 0 go to 
                                      0  2013-01-01    NaN                        5, not inclusive    
                                      1  2013-01-02  93.14
                                      2  2013-01-03  92.97
                                      3  2013-01-04  93.12
                                      4  2013-01-07  93.20


print(oil.iloc[:, :])     returns ->              date  price    *code explain*  ->
                                      0     2013-01-01    NaN
                                      1     2013-01-02  93.14
                                      2     2013-01-03  92.97
                                      3     2013-01-04  93.12
                                      4     2013-01-07  93.20
                                      ...          ...    ...
                                      1213  2017-08-25  47.65
                                      1214  2017-08-28  46.40
                                      1215  2017-08-29  46.46
                                      1216  2017-08-30  45.96
                                      1217  2017-08-31  47.26
                                      [1218 rows x 2 columns]
___________________________________________________________________
'''

# print(oil.iloc[:5,:])
# print(oil.iloc[:, :])

'''
ACCESSING DATA WITH LOC
___________________________________________________________________
The .loc() accessor filters DataFrames by their row and column labels
  - The first parameter accesses rows, and the second accesses columns

print(oil.loc[:5, ['date']])     returns ->          date      *code explain*  ->  ".loc[:5, ['date']]" returns a 2D dataFrame starting index 0 go to index
                                            0  2013-01-01                           5, inclusive.  {'date': [2013-01-01,2013-01-02,2013-01-03,2013-01-04,2013-01-07,2013-01-08]}
                                            1  2013-01-02
                                            2  2013-01-03
                                            3  2013-01-04
                                            4  2013-01-07
                                            5  2013-01-08


print(oil.iloc[:, 'date'])       returns  ->  0    2013-01-01   *code explain*  ->  ".loc[:5, 'date'] returns a 1D index essentially a numpy array.
                                              1    2013-01-02                         [2013-01-01,2013-01-02,2013-01-03,2013-01-04,2013-01-07,2013-01-08]    
                                              2    2013-01-03
                                              3    2013-01-04
                                              4    2013-01-07
                                              5    2013-01-08
                                              Name: date, dtype: str
___________________________________________________________________
'''

print(oil.loc[:5, 'date']) 