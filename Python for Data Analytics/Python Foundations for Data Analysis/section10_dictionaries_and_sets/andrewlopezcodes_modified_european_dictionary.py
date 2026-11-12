'''
#_________________________________________________________
 New European Dictionary
#_________________________________________________________

Hi There, We have an new structure for our European data - 
a nested dictionary. 

Can you help me retrieve some information?


'''

item_ids = [
    10001, 10002, 10003, 10004, 10005, 
    10006, 10007, 10008, 10009
]

item_names = [
    "Coffee", "Beanie", "Gloves", "Sweatshirt", "Helmet",
    "Snow Pants", "Coat", "Ski Poles", "Ski Boots"
]

euro_prices = [
    5.27, 8.79, 17.59, 21.99, 87.99, 
    70.39, 105.59, 87.99, 175.99
]

item_category = [
    "beverage", "clothing", "clothing", "clothing", "safety",
    "clothing", "clothing", "hardware", "hardware",
]

sizes = [
    ["250mL"],
    ["Child", "Adult"],
    ["Child", "Adult"],
    ["XS", "S", "M", "L", "XL", "XXL"],
    ["Child", "Adult"],
    ["XS", "S", "M", "L", "XL", "XXL"],
    ["S", "M", "L"],
    ["S", "M", "L"],
    [5, 6, 7, 8, 9, 10, 11],
    ["S", "M", "L"],
    [5, 6, 7, 8, 9, 10, 11],
    ["NA"],
    ["S", "M", "L", "Powder"],
]

# Note: this is a dictionary comprehension - we will learn this syntax in the next section

euro_data = {
    item_id: {"name": name, "price": price, "category": category, "sizes": sizes}
    for item_id, name, price, category, sizes in zip(
        item_ids, item_names, euro_prices, item_category, sizes
    )
}

euro_data

'''
# Lookup Data
__________________________________________________

Can you check the price for item 10009? I want to 
make sure we loaded the data correctly.
'''
print(euro_data[10009]['price'])

'''
 European Sizes
#__________________________________________________ 

Now can you change the size for the boots (item 10009)
to European shoe sizing? 

The European sizes are in a list below.

'''

boot_sizes = [37, 38, 39.5, 40.5, 41.5, 43.5, 44.5, 46.5]
euro_data[10009]['sizes'] = boot_sizes


'''
 Size Dictionary
#_____________________________________________________
Thanks for you help. The last thing I need is a dictionary 
with item names as keys, and sizes (keep them in a list) 
as the values.

'''

product_sizes = {}
for index, product in enumerate(euro_data.values()):
  product_sizes[product['name']] = product['sizes']

print(product_sizes)