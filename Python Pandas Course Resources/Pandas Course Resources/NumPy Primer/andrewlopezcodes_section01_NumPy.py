'''
 Assignment 1: Array Basics
________________________________________________________________
Hi there,

Can you import Numpy and convert the following list comprehension 
(I just learned about comprehensions in an awesome course by Maven) 
into an array?

[x * 10 for x in range(1, 11)]

Once you've done that report the following about the array:
* The number of dimensions 
* The shape
* The number of elements in the array
* The type of data contained inside
'''
import numpy as np
import numpy.random as default_rng

my_list = [x * 10 for x in range(1, 11)]
# print(my_list)
my_list2 = np.array(my_list)

# print(my_list2)
# print(f'ndim -> (array dimensions): {my_list2.ndim}')
# print(f'shape -> (array shape): {my_list2.shape}')
# print(f'size -> (array size): {my_list2.size}')
# print(f'dtype -> (array data type): {my_list2.dtype}')


'''
 Assignment 2: Array Creation
____________________________________________________________________
Thanks for your help with the first piece - I'm starting to 
understand some of the key differences between base Python data types 
and NumPy arrays. 

Does NumPy have anything like the range() function from base Python?

If so: 
* create the same array from assignment 1 using a NumPy function. 
* Make it 5 rows and 2 columns. 
* It's ok if the datatype is float or int.
'''
my_list3 = np.array(range(1, 11)) * 10
# print(my_list3)
my_list4 = my_list3.reshape(5, 2)
# print(my_list4)

'''
Are there any NumPy functions that can create arrays so
we don't have to convert from a Python list? Recreate 
the array from the first assignment but make it 
5 rows by 2 columns
'''

my_list = [x * 10 for x in range(1, 11)]

my_list5 = np.arange(1, 11,1).reshape(5,2) * 10
# print(my_list5)

my_list6 = np.linspace(10, 100, 10).reshape(5,2)
# print(my_list6)

'''
Create an array of random numbers between 0 and 1,
in a 3X3 shape.
'''

rng = np.random.default_rng(448)
randomArray = rng.random(9).reshape(3,3)
# print(randomArray)

'''
Can you slice and dice the random array we created in the last exercise?

First two 'rows'
first 'column'
second number in third 'row'
'''

# print(randomArray[1:,:])            # First two 'rows'
# print(randomArray[:, 0:1])          # First 'column'
# print(randomArray[2:, 1:2])         # second number in third 'row'

'''
prices = np.array([5.99,6.99,22.49,99.99,4.99,49.99])

1. Add, a flat shipping cost of 5 to the prices array to get the 
total amount owed.

2. Create a random array
rng = np.random.default_rng(448)
randomArray = rng.random(9)
discountPercent = randomArray

3. to get percent owed, subtract the first 6 number in discountPercent
from 1, 

4. then multiply the percent owed by total to get the final amount owed
'''
#1 
prices = np.array([5.99,6.99,22.49,99.99,4.99,49.99])
total = prices + 5
# print(total)

#2
rng = np.random.default_rng(448)
randomArray = rng.random(9)
discountPercent = 1 - randomArray[0:6]
final_owed = total * discountPercent
# print(final_owed.round(2))

'''
 Assignment 5: Filtering Arrays
___________________________________________________________________________
Filter the product array to only include those with prices greater than 25.

Modify your logic to include cola, despite it not having a price greater 
than 25. 
Store the elements returned in an array called `fancy_feast_special`.

Next, create a shipping cost array where the cost is 0 if price is greater 
than 20, and 5 if not. 

'''

products = np.array(
    ["salad", "bread", "mustard", "rare tomato", "cola", "gourmet ice cream"]
)

prices = np.array([5.99,6.99,22.49,99.99,4.99,49.99])
# print(products[prices > 25])

fancy_feast_special =  (prices > 25) | (products == 'cola')
# print(products[fancy_feast_special])

shipping_costs = np.where(prices > 20, 0, 5)
# print(shipping_costs)

'''
 Assignment 6: Aggregating and Sorting Arrays
_______________________________________________________________________________
First, grab the top 3 highest priced items in our list. 

Then, calculated the mean, min, max, and median of the top three prices.

Finally, calculate the number of unique price tiers in our `price_tiers` array.
'''
prices = np.array([5.99,6.99,22.49,99.99,4.99,49.99])
sortedPrices = np.sort(prices)
print(sortedPrices[3:])
print
print(f'Top 3 Price Stats\nMean: {sortedPrices.mean()}\nMin: {sortedPrices.min()}\nMax: {sortedPrices.max()}\nMedian: {round(np.median(sortedPrices[3:]),2)}' )

price_tiers = np.array(["budget", "budget", "mid-tier", "luxury", "mid-tier", "luxury"])
print(f'Unique Price Tiers: {np.unique(price_tiers)}\nNumber of Unique Price Tiers: {len(np.unique(price_tiers))}')