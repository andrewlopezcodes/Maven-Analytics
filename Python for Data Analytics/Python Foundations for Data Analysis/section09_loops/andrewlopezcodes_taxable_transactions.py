'''
Can you apply sales tax to all of the transactions?

The tax rate is 8%. 

Once we've calculated the taxes, we'll need to add them to their subtotals and calculate the the total invoice value.

Your code should produce two lists.

* `taxes`:The first should be a list of the tax amounts on each transaction, rounded to the nearest .01.

* `totals`: The second should be a list where each element is subtotal[i] + tax[i]
'''

sales_tax = .08
subtotals = [15.98, 899.97, 799.97, 117.96, 5.99, 599.99, 24.99, 1799.94, 99.99]
taxes = []
totals = []

for i, subs in enumerate(subtotals):
  tax = round(subtotals[i] * sales_tax, 2)
  taxes.append(tax)
  total = round((subtotals[i] + taxes[i]),2)
  totals.append(total)

print(f"taxes = {taxes}\n totals = {totals}")