"""
#______________________________________________________________________
  Apply Discounts for Multi-Order Customers
#______________________________________________________________________

We need to apply a 10% discount to every transaction in the list below.

Assign the discounted transactions to a new list: `discounted_prices`.
"""


orders_c00001 = [1799.94, 29.98, 99.99]
orders_c00004 = [15.98, 119.99]
orders_c00006 = [24.99, 24.99]
orders_c00008 = [649.99, 99.99]
orders_c00010 = [599.99, 399.97]

multi_order_customers = [
    [1799.94, 29.98, 99.99],
    [15.98, 119.99],
    [24.99, 24.99],
    [649.99, 99.99],
    [599.99, 399.97]
]

multi_order_customers

discount = .10
discounted_princes = []
for order in multi_order_customers:
  subtractedCollector = []
  for individualOrder in order:
    discounted = individualOrder * discount
    subtracted = round(individualOrder - discounted,2)
    subtractedCollector.append(subtracted)
  discounted_princes.append(subtractedCollector)


print(f"The discounted prices = {discounted_princes}")