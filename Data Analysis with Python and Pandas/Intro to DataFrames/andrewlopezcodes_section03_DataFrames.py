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
# print(transactions)
# print(transactions.shape)
# print(transactions.columns)
# print(transactions.dtypes)


'''
 Assignment 2: Exploring DataFrames
___________________________________________________________________________
Hello!

* Can you quickly inspect the first 5 rows of the transactions data? 

* Then, dive a bit more deeply into the data and check if there are any missing values.
* What about the number of unique dates? I want to make sure we didn’t leave any out.
* Finally, can you report the mean, median, min and max of “transactions”?  I want to check for any anomalies in our data.

___________________________________________________________________________

'''

# print(transactions.head())
# print(transactions.info(show_counts=True))
print(transactions.describe(include='all').round())