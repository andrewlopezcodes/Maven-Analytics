'''
#____________________________________________
 Help with European Data
#____________________________________________

Below is our product dictionary, `item_dict`. We need to 
use it to get some data for our European team.


'''

item_dict = {
    10001: ('Coffee', 5.99, 'beverage', ['250mL']),
    10002: ('Beanie', 9.99, 'clothing', ['Child', 'Adult']),
    10003: ('Gloves', 19.99, 'clothing', ['Child', 'Adult']),
    10004: ('Sweatshirt', 24.99, 'clothing', ['XS', 'S', 'M', 'L', 'XL', 'XXL']),
    10005: ('Helmet', 99.99, 'safety', ['Child', 'Adult']),
    10006: ('Snow Pants', 79.99, 'clothing', ['XS', 'S', 'M', 'L', 'XL', 'XXL']),
    10007: ('Coat', 119.99, 'clothing', ['S', 'M', 'L']),
    10008: ('Ski Poles', 99.99, 'hardware', ['S', 'M', 'L']),
    10009: ('Ski Boots', 199.99, 'hardware', [5, 6, 7, 8, 9, 10, 11])
}

'''
 Size Counts
#_________________________________ 

First I need a dictionary with the item numbers in `item_dict`
as keys, and the number of sizes available for each item as 
the values. Sizes are stored in lists at the end of each 'row' 
of data. Key 10001 has a list with one size, 250ml at the end.

'''

size_counts = {}
itemKeys = list(item_dict)

for index, itemkey in enumerate(itemKeys):
  lastValue = list(item_dict[itemkey][-1])
  size_counts[itemKeys[index]] = len(lastValue)
print(size_counts)

'''
 New Size Options
 #_________________________________ 

Now that you've done that, we need to add two products 
to `size_counts`:

* Item 10010 has 4 sizes.
* Item 10011 has 7 possible sizes.
'''

size_counts.update({'10010': 4, '10011': 7})
print(size_counts)


'''
 Euro Pricing
#_________________________________ 
Finally, pull the prices out of `item_dict` and create a 
list with converted Euro pricing. 
Use an exchange rate of .88.
'''
exchange_rate = .88
euro_prices = []
itemKeys = list(item_dict)

for index, itemKey in enumerate(itemKeys):
  secondValue = item_dict[itemKey][1]
  euroPrice = euro_prices.append(round(secondValue * exchange_rate, 2))

print(euro_prices)
