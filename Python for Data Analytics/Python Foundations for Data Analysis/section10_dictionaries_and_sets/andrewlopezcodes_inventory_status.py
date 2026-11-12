'''
#______________________________________________________
 Inventory Status
#______________________________________________________

Our products and inventory levels are in the lists below.

'''

items = ['skis', 'snowboard', 'goggles', 'boots']
inventory = [10, 0, 0, 7] 

'''
Inventory Status Dictionary

Can you create a dictionary that:

* Stores item name as keys
* Values are 'sold out' if inventory is 0, and 'in stock' if not?

Don't create this by writing out all the key value pairs!

Thanks!
'''

inventory_status = {}

for i, item in enumerate(items):
  if inventory[i] != 0:
    inventory_status[items[i]] = 'in stock'
  else:
    inventory_status[items[i]] = 'sold out'

print(inventory_status)