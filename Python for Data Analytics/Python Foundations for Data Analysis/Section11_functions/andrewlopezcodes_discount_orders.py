'''
 Apply A Special Discount
_____________________________________________________
We need to apply a discount for customers who purchased 
more than 500 dollars worth of product – they’re starting 
to complain it hasn’t been applied. They need to get 10% 
off on their orders.

Can you quickly apply a discount? 
Store the new prices in a list called `discounted_subtotals`.
'''

subtotals = [15.98, 899.97, 799.97, 117.96, 5.99, 599.99]

discounted_subtotals = map(
  lambda x: round((x - (x * .06)), 2) 
  if x > 500 
  else x, 
  subtotals)
print(list(discounted_subtotals))