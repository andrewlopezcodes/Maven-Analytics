'''
 Transaction Dictionary Creator
_____________________________________________________________
Hi there, we need to make some final updates to our tax 
calculator function.

We need a function takes a list of customer_ids, a list of 
subtotals, and a tax rate, that calls the tax_calculator on 
a list of subtotals, then returns a dictionary with customer_IDs 
as keys, and the lists returned from tax_calculator as the values.

A dictionary comprehension would be very helpful here.

Your function will need the following arguments:

* customer_ids - a list of strings
* subtotals - a list of numbers
* tax_rate - the tax rate which will be passed to tax_calculator

The output will be a dictionary with:

* Customer IDs as keys
* [subtotal, tax, total] as values


'''

from tax_calculator import tax_calculator
import numpy as np


customer_ids = ['C00004', 'C00007', 'C00015', 'C00016', 'C00020', 'C00010']

subtotals = [15.98, 899.97, 799.97, 117.96, 5.99, 599.99]

tax_rate = .08


def transaction_dict_creator(x, y, z):
  subz2 = list(map(lambda y: tax_calculator(y, z), y))
  dictMaker = dict(zip(x,subz2))
  return dictMaker



print(transaction_dict_creator(customer_ids, subtotals, tax_rate))