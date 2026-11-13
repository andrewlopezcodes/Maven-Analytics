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
print(rng.normal(73, 5, 10))    #result -> [67.5063021  66.85650087 71.21859854 70.14466119 74.38339875 78.87574052 59.70007029 73.82614671 77.14231196 74.49906013]



