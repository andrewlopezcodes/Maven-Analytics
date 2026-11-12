'''
Weekend Sales Follow-Up Analysis
______________________________________________________

Hey there, 

There are three lists below representing the customers 
who made purchases on Friday, Saturday, and Sunday.

We want to target customers who made purchases on 
Friday and either Saturday or Sunday with follow up 
promotions.

'''

friday_customers = [
    'C00004', 'C00007', 'C00015', 'C00016', 'C00020',
    'C00010', 'C00006', 'C00001', 'C00003', 'C00014',
    'C00001', 'C00001', 'C00005', 'C00008', 'C00013'
]

saturday_customers = [
    'C00004', 'C00017', 'C00019', 'C00002', 'C00008',
    'C00021', 'C00022'
]

sunday_customers = ['C00006', 'C00018', 'C00018', 'C00010', 'C00016']

'''
 Collect Unique Weekend Customers
___________________________________________________ 

First, can you gather all the unique customers from the 
weekend (`saturday_customers` and `sunday_customers`)? 
Create a set called `weekend_set` to store them.
'''

fridaySet = set(friday_customers)
saturdaySet = set(saturday_customers)
sundaySet = set(sunday_customers)

weekendSet = saturdaySet.union(sundaySet)

print(weekendSet)

'''
 Friday Customers Who Came Back During the Weekend
 _______________________________________________________

Now that you've got that, can you see which customers 
made a purchase on Friday AND made a purchase during the 
weekend?
'''

print(fridaySet.intersection(weekendSet))