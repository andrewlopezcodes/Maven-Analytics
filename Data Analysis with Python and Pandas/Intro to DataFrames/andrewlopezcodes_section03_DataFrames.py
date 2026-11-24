import numpy as np
import pandas as pd

'''
 Assignment 1: DataFrame Basics
___________________________________________________________________________


Hi there!

Can you read in the transactions dataset and report on:

* The number of rows and columns
* The names of the columns
* The datatypes of each column

path = "../retail/transactions.csv"
___________________________________________________________________________

'''

path = "transactions.csv"
transactions = pd.read_csv(path)
print(transactions)
print(transactions.shape)
print(transactions.columns)
print(transactions.dtypes)