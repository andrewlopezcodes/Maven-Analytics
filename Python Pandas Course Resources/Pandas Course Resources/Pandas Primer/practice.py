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
_________________________________________________________________
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

# print(sales_series.reset_index(drop=True))



'''
Filtering Series
_____________________________________________________________
You can filter a Series by passing a logical test into the .loc[]
accessor like arrays

sales_series.loc[sales_series > 0]
_________________________________________________________________
'''
sales = [0,5,155,0,518]
items = ['coffee', 'coffee', 'tea','coconut','sugar']
sales_series = pd.Series(sales, index=items, name="Sales")
# print(sales_series)
# print(sales_series.loc["coffee"])


# print(sales_series.loc[sales_series > 0])
mask = (sales_series > 0) & (sales_series.index == "coffee")
# print(sales_series.loc[mask])

'''
Logical Operators & Methods
_____________________________________________________________
You can use these operators & methods to create boolean filters
for logical test

Description           Python Operator   Pandas Method
----------------------------------------------
Equal                 ==              .eq()
Not Equal             !=              .ne()
Less Than or Equal    <=              .le()
Less Than             <               .lt()
Greater Than or Equal >=              .ge()
Greater Than          >               .gt()
Membership Test       in              .isin()
Inverse Membership    not in          ~.isin() 
Inverse                               ~ the '~' inverts boolean values
_________________________________________________________________
'''
# print(sales_series == 5)    #Python Operator
# print(sales_series.eq(5))   #Pandas Method

# print(sales_series.index.isin(['coffee','tea']))
# print(~sales_series.index.isin(['coffee','tea']))

# print(sales_series.gt(2))
# print(~sales_series.gt(2))
# print(sales_series.loc[sales_series > 2])
# print(sales_series.loc[~(sales_series > 2)])

'''
Sorting Series
_____________________________________________________________
You can sort Seris by their values or their index

1. The .sort_values() method sorts a Series by its values in 
  ascending order
2. The .sort_index() method sorts a Series by its values in 
  ascending order
3. The .sort_values(ascending= False) method sorts a Series by
  by its values in descending order


_________________________________________________________________
'''

# print(sales_series.sort_values())
# print(sales_series.sort_values(ascending= False))
# print(sales_series.sort_index())
# print(sales_series.sort_index(ascending= False))

'''
Arithmetic Operators & Methods
_____________________________________________________________
You can use these operators & methods to perform numeric 
operations on Series

Description           Python Operator   Pandas Method
----------------------------------------------
Addition              +                 .add
subtraction           -                 .sub() or .subtract()
Multiplication        *                 .mul() or .multiply()
Division              /                 .div() or .divide() or truediv()
Floor Division        //                .floordiv()
Modulo                %                 .mod()
Exponentiation        **                .pow()
_________________________________________________________________
'''

monday_sales = pd.Series([0,5,155,0,518])

# print(monday_sales)
# print(monday_sales + 2)
# print(monday_sales.add(2))

# print("$"+ monday_sales.astype("float").astype('string'))

my_series = pd.Series(
  [1,np.nan,2,3,4], 
  index=['day 0','day 1','day 2','day 3','day 4']
  )


# print(my_series)
# print(my_series + 1)
# print(my_series.add(1))
# print(my_series.add(1, fill_value=0))       # *code explain*  -> 'fill_value=0' will replace any missing value
#                                             #                     with a value of '0' which will allow the 
#                                             #                     '.add' operator to process 

my_series2 = my_series.add(1, fill_value=0).astype('int')
# print(my_series2 /2)
# print(my_series.add(my_series2, fill_value=0))

'''
String Methods
_____________________________________________________________
The Pandas str accessor lets you access many string methods
  - These methods all return a Series (split returns multiple series)

String Method                     Python Operator   Pandas Method
-------------------------------------------------------

.strip(), .lstrip(),.rstrip()                 Removes all leading and/or trailing characters
                                              (spaces by default)

.upper(), .lower()                            Converts all characters to upper or lower case

.slice(start:stop:step)                       Applies a slice to the strings in a Series

.count("string")                              Counts all instances of a given string

.contains("string")                           Returns True if a given string is found; False if not

.replace("a", "b")                            Replaces instances of string "a" with string "b"

.split("delimiter", expand=True)              Splits strings based on a given delimiter string, and
                                              returns a DataFrame with a Series for each split

.len()                                        Returns the length of each string in a Series

.startswith("string"), .endswith("string")    Returns True if a string starts or ends with given
                                              string; False if not
_________________________________________________________________
'''

prices = pd.Series(['$3.99','$5.99','$22.99','$7.99','$33.99'])
# print(prices)

# print(prices.str.contains('3'))

clean = prices.str.strip('$').astype("float")
# print(clean)

string_series = pd.Series(['day 0','day 1','day 2','day 3','day 4'])

# print(string_series.str[-1])                          # returns ->  0    0      *code explain*  -> .str is called the StrDescriptor
#                                                       #             1    1                          it forces the 'str' properties onto
#                                                       #             2    2                          the values of a pandas series index.
#                                                       #             3    3                          ex: the value 123 in ('int') -> "123" in ('str')
#                                                       #             4    4
#                                                       #             dtype: str

# print(string_series.str.split(" "))                   # returns ->  0    [day, 0]
#                                                       #             1    [day, 1]
#                                                       #             2    [day, 2]
#                                                       #             3    [day, 3]
#                                                       #             4    [day, 4]
#                                                       #             dtype: object

# print(string_series.str.split(" ", expand=True))      # returns ->       0  1
#                                                       #             0  day  0
#                                                       #             1  day  1
#                                                       #             2  day  2
#                                                       #             3  day  3
#                                                       #             4  day  4


'''
Numeric Series Aggregation Methods
_____________________________________________________________
You can use these methods to aggregate numerical Series

String Method             Description
-------------------------------------------------------
.count()                  Returns the number of items

.first(), .last()         Returns the first or last item

.mean(), .median()        Calculates the mean or median

.min(), .max()            Returns the smallest or largest value

.argmax(), .argmin()      Returns the index for the smallest or largest values

.std(), .var()            Calculates the standard deviation or variance

.mad()                    Calculates the mean absolute deviation

.prod()                   Calculates the product of all the items

.sum()                    Calculates the sum of all the items

.quantile()               Returns a specified percentile, or list of percentiles

.quartile()               Returns a quantile sorted into Q1(0.25), Q2/Median(0.50), Q3(0.75)
_________________________________________________________________
'''
sales_series.loc['coconut'] = np.nan
# print(sales_series)
# print(sales_series.sum())
# print(sales_series.loc['coffee'].sum())
# print(sales_series.quantile([.25,.5,.75]))

transactions = pd.read_csv("C:\\Users\\sneak\\Desktop\\Maven Analytics\\Python Pandas Course Resources\\Pandas Course Resources\\Pandas Primer\\transactions.csv")
transactions_series = pd.Series(transactions['transactions'])
# print(transactions_series.iloc[:5])
# print(transactions_series.count())
# print(transactions_series.iloc[:5].quantile([.5]))



'''
Categorical Series Aggregation Methods
_____________________________________________________________
You can use these methods to aggregate and analyze categorical Series

String Method             Description
-------------------------------------------------------
unique()                  Returns an array of unique items in a Series
.nunique()                Returns the number of unique items
.value_counts()           Returns a Series of unique items and their frequency
_________________________________________________________________
'''
items = pd.Series(['coffee', 'coffee', 'tea','coconut','sugar'])
print(items)                                            # returns ->  0     coffee
                                                        #             1     coffee
                                                        #             2        tea
                                                        #             3    coconut
                                                        #             4      sugar
                                                        #             dtype: str  


print(items.value_counts())                             # returns ->  coffee     2                        *code explain*  -> returns how many of each 
                                                        #             tea        1                                           items are in the series
                                                        #             coconut    1
                                                        #             sugar      1
                                                        #             Name: count, dtype: int64

print(items.value_counts(normalize=True))               # returns ->  coffee     0.4                      # *code explain*  -> Returns the percentage of
                                                        #             tea        0.2                                           each item's value occurrence in
                                                        #             coconut    0.2                                           the series (ex:  coffee   0.4  = 40%)
                                                        #             sugar      0.2                                                            tea      0.2  = 20% 
                                                        #             Name: proportion, dtype: float64


print(pd.Series.astype('int' or 'str' or 'float').value_counts(normalze=True))                         # *code explain*  -> takes in a series where the value is
                                                        #                                                                    a datatype and using astype() method
                                                        #                                                                    converts it to another data type for
                                                        #                                                                    calculations.
                                                        #                                                                    Then the .value_counts(normalize=True)
                                                        #                                                                    returns the percentage of each values
                                                        #                                                                    occurrence in the series
                                                        #    
                                                        #                                                                    ex: value is '16' 
                                                        #                                                                    astype('int')    -> 16
                                                        #                                                                    astype('float')  -> 16.0


print(items.unique())                                     # returns ->  0     coffee                        *code explain*  -> returns a pandas array with the 
                                                          #             1     coffee                                           index position and .
                                                          #             2        tea                                           <StringArray>['coffee','tea','coconut','sugar']
                                                          #             3    coconut
                                                          #             4      sugar
                                                          #             dtype: str>

print(items.nunique())                                   # returns ->  Length: 4, dtype: str