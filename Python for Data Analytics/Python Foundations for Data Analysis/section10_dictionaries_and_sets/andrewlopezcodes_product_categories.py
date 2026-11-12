'''
#___________________________________________________
 Product Category Analysis
#___________________________________________________

Hi There,

I've supplied the code to create our European item dictionary below.


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

'''
 Unique Categories
#____________________________________________________

Can you collect the unique item categories from the 
dictionary `euro_items`? 

It's the first step in my analysis.
'''

unique_categories = list(set(item_category))
print(unique_categories)

'''
 How many categories are there?
_______________________________________________________

Now that you have that, how many categories are there?
'''

print(len(unique_categories))

'''
 Is 'outdoor' in our set of categories?
______________________________________________________
Outdoor equipment is popular in Europe - can you see 
if we've added items from that category based on the 
unique categories you created? 

'''
print('outdoor' in unique_categories)