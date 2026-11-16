import numpy as np

sales = [[0,5,155,0,518],[0,1827,616,317,325],[0,1827,616,317,325]]

sales_array = np.array(sales)
# print(sales_array)

# print(f"ndim -> (numbers of dimensions): {sales_array.ndim}")
# print(f"shape -> (numbers of dimensions): {sales_array.shape}")
# print(f"size -> (numbers of dimensions): {sales_array.size}")
# print(f"dtype -> (numbers of dimensions): {sales_array.dtype}")


array = np.array(range(5))
array2 = np.array([range(5), range(5)])
# print(array2.shape)

'''
______________________________________________________________________
'''

array3 = np.ones((2,5),'int64')
# print(array3)
array4 = np.zeros((2,5), 'int64' )
# print(array4)
array5 = np.arange(1, 7, 2) # arange(start, stop, step) stop not inclusive
# print(array5)
array6 = np.linspace(1.5,2.5, 11) # linspace(start, stop, equal distant number of spaces between start and stop including stop number) think a chart axis  
# print(array6)
array7 = np.arange(1, 21, 1).reshape(4,5 ) # arange(start, stop, step) stop not inclusive | 
                                            # reshape(rows, cols) rearrange the array by multiples 
                                            # of the number of items created by arange()
# print(array7)

'''
_________________________________________________________________________
'''

# np.default_rng(seed)          -> Creates a random number generator (the seed is for reproducibility)
# rng.random(n)                 -> returns n random numbers from a uniform distribution between 0 and 1
# rng.normal(mean, stdev, n)    -> returns n random numbers from a normal distribution with a given mean and standard deviation

from numpy.random import default_rng

rng = np.random.default_rng(616)

rng.random(10)                  # random() gives you floats between 0 and 1
# print(rng.random(10))         #result -> [0.33966929 0.062511 0.35706816 0.20250319 0.4305179  0.1033163 0.52396562 0.80203893 0.07529808 0.15143375]

rng.integers(0, 20, 100)        #  integers(start, end, how many numbers to display ) 
                                #  *code-meaning* -> display 100 numbers, randomly chosen from numbers 0 to 20

# print(rng.integers(0, 20, 100)) 


rng.normal(73, 5, 10)
# print(rng.normal(73, 5, 10))    #result -> [67.5063021  66.85650087 71.21859854 70.14466119 74.38339875 78.87574052 59.70007029 73.82614671 77.14231196 74.49906013]

'''
Indexing & Slicing Dimensional Arrays
______________________________________________________________________________________
'''
# Single Dimensional Arrays
# array[index]                    -> indexing to access a single element (0 - indexed)
# array[start : stop : step size] -> slicing to access a series of elements (stop is not inclusive)


product_array = np.array(['fruits','vegetables','cereal','dairy','eggs','snacks','beverages','coffee','tea','spices'])
productS_array = np.array(['fruits','vegetables','cereal','dairy','eggs','snacks','beverages','coffee','tea'])
# print(product_array[-1])          # result -> "spices"
# print(product_array[5::2])        # result -> ['snacks', 'coffee', 'spices']


# Multi Dimensional Arrays
# array[row index, column index]  -> indexing to access a single element (0 - indexed)
# array[start : stop : step size, start : stop : step size] -> slicing to access a series of elements


product_array2D = product_array.reshape(2, 5)
# print(product_array2D)              # reuslt -> [['fruits' 'vegetables' 'cereal' 'dairy' 'eggs']
                                      #           ['snacks' 'beverages' 'coffee' 'tea' 'spices']]

# print(product_array2D[1, 2])        # result -> 'coffee'
# print(product_array2D[:, 2:])       # result ->  [['cereal' 'dairy' 'eggs']
                                      #            ['coffee' 'tea' 'spices']]
                                      # *code explain* -> [:, <- (grab all rows) 2 <- (start at index 2)  : <- (semicolon blank :" " go all the way to the end)]

# print(product_array2D[1:, :])       # result ->   ['snacks','beverages','coffee','tea','spices']
array3d = productS_array.reshape(3,3)
# print(array3d)
# print(array3d[2:, 1:2])

#___________________________________________________________________________

# print(sales_array)
# print(sales_array != 0)                                             # Performing a logical test on a NumPy array returns a Boolean array with the results of the logical test on each array element
# print(sales_array[sales_array != 0])                                # indexing an array with a Boolean array returns an array with the elements where the Boolean value is True

# print(sales_array[(sales_array == 616) | (sales_array < 100)])      # returns -> [  0   5   0   0 616   0 616] using "|" as "or"
# print(sales_array[(sales_array > 100) & (sales_array < 500)])       # returns -> [155 317 325 317 325] using "&"" as "and"

# booleanMask1 = (sales_array == 616) | (sales_array < 100)           # returns -> [  0   5   0   0 616   0 616] storing the boolean statement in a variable is called a boolean mask
# print(sales_array[booleanMask1])

# booleanMask2 = (sales_array > 100) & (sales_array < 500)            # returns -> [155 317 325 317 325] storing the boolean statement in a variable is called a boolean mask
# print(sales_array[booleanMask2])

short_products = np.array(['fruits', 'vegetables', 'cereal', 'dairy', 'eggs'])
small_sales_array = np.array([0, 5, 155, 0, 518])
# print(short_products[small_sales_array > 0])                          # returns -> ['vegetables' 'cereal' 'eggs']
                                                                      # *code explain* -> Using "small_sales_array" as a Boolean array, 
                                                                      #                   "[small_sales_array > 0]" returns -> [False, True, True, False, True}
                                                                      #                   the indexes which are "True", [1,2,4] filter the "short_products" array 
                                                                      #                   and returns short_products[1, 2, 4] -> ['vegetables' 'cereal' 'eggs']


# print(f'small_sales_array = true index {np.argwhere(small_sales_array> 0)[0]}  -> short_products[1] {short_products[1]}\nsmall_sales_array = true index {np.argwhere(small_sales_array> 0)[1]} -> short_products[2] {short_products[2]}\nsmall_sales_array = true index {np.argwhere(small_sales_array> 0)[2]} -> short_products[4] {short_products[4]}]')                                    


'''
  ARRAY AGGREGATION METHODS
  __________________________________________________________________________________
'''
# print(sales_array.sum())                                              # returns -> 6848
# print(sales_array.sum(axis=0))                                        # returns -> [   0 3659 1387  634 1168]
                                                                      # *code explain* -> sums the matrix columns and returns an array with the summed totals
                                                                      #                   [   0    5  155    0  518]
                                                                      #                   [   0 1827  616  317  325]
                                                                      #                   ==========================
                                                                      #         SUM TOTAL [   0 3659 1387  634 1168]

# print(sales_array.sum(axis=1))                                        # returns -> [ 678 3085]
                                                                      # *code explain* -> sums the matrix rows and returns an array with the summed totals
                                                                      #                                               Totals
                                                                      #                   [   0    5  155    0  518] |  678
                                                                      #                   [   0 1827  616  317  325] | 3085


rng = np.random.default_rng(616)                                      # *code explain* -> random number generator from numpy using a seed of 616
price = (rng.random(10) * 10).round(2)                                # *code explain* -> assign to variable price 10 random numbers between 0 -1 multiplied 
                                                                      #                   by 10 and rounded to 2 decimal places
# print(price)                                                          # returns ->  [3.97 8.66 4.6  3.06 5.74 0.89 8.82 7.32 7.32 5.62]

inventory = rng.integers(0, 100, 10)                                  # *code explain* -> random number generator for integers 
                                                                      #                   low number = 0 high number = 100 how many numbers to generate = 10
# print(inventory)                                                      # returns -> [80 33 60  6 31 35 16 20 29 43]

# print(price.mean())                                                   # returns -> 5.6
# print(inventory.mean())                                               # returns -> 35.3
# print(price * inventory)

'''
 Array Functions
 ______________________________________________________________________

np.median(array) #returns the median value in an array
np.percentile(array, n) #returns a value in the nth percentile in an array
np.unique(array) #returns the unique values in an array
np.sqrt(array) #returns the square root of each value in an array
'''
'''
  Sorting Arrays
_________________________________________________________________________
sorting in place / array.sort()     -> changes the original array when sorting
sorting not in place / np.sort(array)  -> does not change original array
'''

sales_array = np.array([0,5,155,0,518,0,1827,616,317,325]).reshape(2,5)
# print(sales_array)                                                              # returns -> [[0,5,155,0,518],[0,1827,616,317,325]] (before sorting in place)
# print(np.sort(sales_array))                                                     # returns -> [[0, 0, 5, 155, 518], [0, 317, 325, 616, 1827]] (sorting not in place)
# print(sales_array.sort())                                                       # returns -> None
# print(sales_array)                                                              # returns -> # [[0, 0, 5, 155, 518], [0, 317, 325, 616, 1827]] (after sorting in place)


'''
Vectorization
_______________________________________________________________
'''
def for_loop_multiply_list(list1, list2):                                     # *code explain* -> function that multiplies two Python lists
  product_list =[]
  for element1, element2 in zip(list1, list2):
    product_list.append(element1 * element2)
  return product_list


def multiply_arrays(array1, array2):                                          # *code explain* -> function that multiplies two NumPy arrays
  return array1 * array2

list1 = list(range(1000))
list2 = list(range(1000))

'''
Broadcasting
_________________________________________________________________
Broadcasting lets you perform vectorized operations with arrays of 
different sizes, where NumPy will expand the smaller array to "fit" 
the larger one.

Single values (scalars) can b broadcast into arrays of any dimension
Dimensions with a length greater than one must be the same size
'''

test_array = np.array([[1,2,3], [1,2,3], [1,2,3]])
print(test_array)
print(test_array + 1)
print(test_array + np.array([3,2,1]))
print(test_array + np.array([3,2,1]).reshape(3, 1))