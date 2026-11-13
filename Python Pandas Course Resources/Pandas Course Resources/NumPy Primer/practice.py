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
print(array2.shape)