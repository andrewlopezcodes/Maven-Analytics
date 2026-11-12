'''
 Total Cost of European Items
___________________________________________________________
Below is the code to recreate our European item dictionary.

Run the cells below, then follow the instructions below.
'''

import numpy as np

# Data for dictionary - run this cell and the followwing to create it

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

# This is a dictionary comprehension
# We'll see an example after this assignment!

euro_data = {
    item_id: [name, price, category, sizes]
    for item_id, name, price, category, sizes in zip(
        item_ids, item_names, euro_prices, item_category, sizes
    )
}

print(sum([value[1] for value in euro_data.values()]))