'''
### Sales Tax by State

We forgot to account for the fact that different states have different tax rates, so we need to modify our loop we just built. 

We have a list containing the location of each purchase. The transaction `subtotal[i]` took place at `locations[i]`.

The following tax rates should be applied for each location:

* Sun Valley: 8%
* Stowe: 6%
* Mammoth: 7.75%

'''

subtotals = [
    15.98, 899.97, 799.97, 117.96, 5.99, 
    599.99, 24.99, 1799.94, 99.99
]

location = [
    'Sun Valley', 'Stowe', 'Mammoth', 'Stowe', 'Sun Valley', 
    'Mammoth', 'Mammoth', 'Mammoth', 'Sun Valley'
]

location_tax = []
taxes = []
totals = []
for i in location:
  if i == 'Sun Valley':
    location_tax.append(.08)
  elif i == 'Stowe':
    location_tax.append(.06)
  else:
    location_tax.append(.0775)

for e, subs in enumerate(subtotals):
  tax = round((subs * location_tax[e]),2)
  taxes.append(tax)
  total = round((subtotals[e] + taxes[e]),2)
  totals.append(total)

print(f"taxes = {taxes}\ntotals = {totals}")