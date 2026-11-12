'''
 Using the tax calculator!
 _______________________________________________________

Now that we have a working tax calculator, we need to put
it to work.

First, import the tax calculator.
'''
import tax_calculator as tc

'''
 Processing Transactions
________________________________________________________

Apply the tax calculator to the list of subtotals below.

We want to store all of the results in a single list, so 
each list returned from the tax calculator should be a 
list stored in a list called `full_transactions`. Use the 
default tax rate for each transaction.
'''
subtotals = [15.98, 899.97, 799.97, 117.96, 5.99, 599.99]
full_transactions = []

def transactionListMaker(list):
  for index, subs in enumerate(list):   
    full_transactions.append(tc.tax_calculator(subs))
  return full_transactions

print(transactionListMaker(subtotals))

'''
 Transaction Dictionary
_______________________________________________________
Great! Now that you've done that, combine the transactions 
with the customer_ids below into a dictionary.

We want the customer_ids as keys, and the transactions as values.
'''
customer_ids = ['C00004', 'C00007', 'C00015', 'C00016', 'C00020', 'C00010']


customer_dict = dict(zip(customer_ids, full_transactions))
print(customer_dict)