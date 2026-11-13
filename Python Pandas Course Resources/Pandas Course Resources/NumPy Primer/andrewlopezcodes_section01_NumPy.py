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
Recreate the array from the first assignment but make it 
5 rows by 2 columns
'''

my_list = [x * 10 for x in range(1, 11)]

my_list5 = np.arange(1, 11,1).reshape(5,2) * 10
# print(my_list5)


'''
Create an array of random numbers between 0 and 1
'''

rng = np.random.default_rng(448)
randomArray = rng.random(20)
print(randomArray)