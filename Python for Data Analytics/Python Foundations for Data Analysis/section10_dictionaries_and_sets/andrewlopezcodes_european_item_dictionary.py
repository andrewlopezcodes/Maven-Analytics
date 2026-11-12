'''
#_______________________________________________________
 European Item Dictionary
#_______________________________________________________

Hi there, we need to create a European price dictionary. 

The data is stored in the lists below. Run the cell below 
to create the lists you need.

'''


# Data for dictionary 

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
]

'''
Create a dictionary with the `item_ids` as keys and the rest of the data the values. 

We want the values to be in the order of `item_names`,`euro_prices`, `item_category`, `sizes`.
'''

euro_items = dict(zip(item_ids, zip(item_names,euro_prices,item_category,sizes))) 
print(euro_items)