'''
#____________________________________________________
 Snack Dictionary
#____________________________________________________

Hey, the current snack dictionary is below - thanks for your help with this!

Run this first cell to create the `snacks` dictionary.

'''

snacks = {
    'Sally': 'Popcorn',
    'Richard': 'Chocolate Ice Cream',
    'Stuart': 'Apple Pie',
    'Jerry': 'Raisins',
    'Sierra': 'Peanut Butter Cookies'
}

#Can you lookup Stuart's favorite snack?
print(snacks['Stuart'])

'''
Cool, that's one of my favorites too!

Can you make the following changes do the dictionary?

* Add me - 'Alfie', and my favorite snack, 'Cheese and Crackers'.
* Change Jerry's favorite snack to 'Fig Bars'
* Finally, remove Sierra, she never worked here, not sure how she got on the list.
'''

snacks['Alfie'] = 'Cheese and Crackers'
snacks['Jerry'] = 'Fig Bars'
del snacks['Sierra']

print(snacks)
