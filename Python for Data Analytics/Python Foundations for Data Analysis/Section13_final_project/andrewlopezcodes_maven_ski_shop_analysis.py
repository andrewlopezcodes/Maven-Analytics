'''
 Final Project: Black Friday Excel Data
 ____________________________________________________________________
'''

import openpyxl as xl
import tax_calculator
import statistics as stats

# pprint prints dictionaries a bit more nicely than print
from pprint import pprint

'''
 Part 1
_____________________________________________________________________
First, read in maven_ski_shop_data.xlsx

Then, assign the orders worksheet to an intuitive variable name. 
'''

xl.load_workbook(filename='maven_ski_shop_data.xlsx')
workbook = xl.load_workbook(filename='maven_ski_shop_data.xlsx')
# print(workbook.worksheets)
items =       workbook['Item_Info']
inventory =   workbook['Inventory_Levels']
orders =      workbook['Orders_Info']

'''
 Column Printer Function
__________________________________________________________________ 

Since we'll be working with Excel frequently, let's create a helper 
function to print all the rows a specified column.

This will help us view imported data without looking at Excel, and 
review the data we've written into columns without needing to save 
a file to review the changes.

Your function should take two arguments:

* Worksheet where data is located
* Column Letter of data to print

Your function should:

* Print Cell Coordinate (e.g. A1, D4).
* Print the contents of the cell.

Then call your function twice:

* Once to print Order ID (column A in 'Orders_Info')
* Once to print subtotal (column D in 'Orders_Info')
'''

# def column_printer(worksheet, column_letter):
#   for index, cell in enumerate(worksheet[f'{column_letter}'], start=1):
    # print(f'{column_letter}{index}', cell.value)

# print(column_printer(orders, "B"))


'''
 Order Data Dictionary
____________________________________________________________ 

Create a dictionary with all of the information contained in 
the 'Orders_Info' Worksheet.

* The dictionary keys should be Order IDs (Column A)
* The values should a list storing the data in the rest of the columns.
* The columns in the list stored as values should be B, C, D, G, and H (after converting to list). 
* For example: The first order, column H should be the nested list: [10001, 10002]


A few notes:

* Convert the Items_Ordered field into a list (we covered a helpful string method for this)
* This can be done with a dictionary comprehension
* DO NOT INCLUDE EXCEL COLUMN HEADERS
'''

order_dict = {
  orders[f'A{order}'].value:[
    orders[f'B{order}'].value,
    orders[f'C{order}'].value,
    orders[f'D{order}'].value,
    orders[f'G{order}'].value,
    str(orders[f'H{order}'].value).split(', ')
  ]
  for order in range(2, orders.max_row +1 )
}

# pprint(order_dict)


'''
 Sales Tax Calculation (Last time!)
___________________________________________________________________

We need to calculate the sales tax and total amount owed for every 
order in this sheet.

* If location is Sun Valley, apply a sales tax of 8%
* If location is Mammoth, apply a sales tax of 7.75%.
* If location is Stowe, apply a sales tax of 6%

Use the tax_calculator function to apply sales tax to each subtotal.

**Insert** the calculated sales tax and total amounts into your customer 
dictionary immediately after subtotal.

**Tip**: Figure out how to do this once and then loop through the column.
'''

for order in order_dict.values():
  if order[3] == 'Sun Valley':
    transaction = tax_calculator.tax_calculator(order[2], 0.08)
  elif order[3] == 'Mammoth':
    transaction = tax_calculator.tax_calculator(order[2], 0.0775)
  else:
    transaction = tax_calculator.tax_calculator(order[2], 0.06)

  order.insert(3, transaction[1])
  order.insert(4, transaction[2])

# pprint(order_dict)


'''
 Write Sales Tax and Total Into the Excel Sheet
__________________________________________________________________________ 


Great job! Now we just need to write this data into the workbook.

Write the sales tax and total you just calculated into the workbook, then save!

Call this workbook 'maven_ski_shop_data_fixed'.

**Tip:** There are a few ways to do this. As always, be patient, solve one 
  step at a time.
'''

for index, order in enumerate(order_dict.values(), start=2):
  orders[f'E{index}'] = order[3]
  orders[f'F{index}'] = order[4]

# workbook.save('andrewlopezcodes_maven_ski_shop_data_fixed.xlsx')



'''
 Part 2

 Analysis Time!
___________________________________________________________________

Now that we've fixed the data - it's time to perform analysis on 
our sales.

Our starting point will be the order_dict we created, after we added 
the taxes and totals columns.

Our first step will be to write a function that calculates the sum of a 
'column' of data in our dictionary.

A 'column' for example, would be subtotals, which is at index 2 in 
the list stored as our dictionary values.

Your function should take the following arguments:

* Column Index (the index of the data of interest in the list stored 
in our dictionary values)

* Dictionary Name

It should output:

* The sum of values in the column (rounded to two decimal places)

Assume only numeric values will be in the column (You can develop 
cleaning logic later :D)

**Tip:** Use a list comprehension to retrieve the values of interest.

'''
# print(order_dict[100001]) 

'''
 Sum The Subtotal, Tax, and Total Columns 
__________________________________________________________________
Now that we have our column sum function, calculate the sum of:

* Subtotals
* Taxes
* Totals
'''

def column_sum(column_index, dictionary):
  return round(sum([value[column_index] for value in dictionary.values()]), 2)

# print(f'the sum of column B is : ${column_sum(2, order_dict)}')
# print(f'the sum of column c is : ${column_sum(3, order_dict)}')
# print(f'the sum of column D is : ${column_sum(4, order_dict)}')

'''
 What is the average of our subtotals?
____________________________________________________________________
Calculate the average value of our transactions.

Remember that each entry in your dictionary is one order.
'''

def column_avg(column_index, dictionary):
  return round(stats.mean([value[column_index] for value in dictionary.values()]), 2)

# print(f'the average of column B is : ${column_avg(2, order_dict)}')
# print(f'the average of column C is : ${column_avg(3, order_dict)}')
# print(f'the average of column D is : ${column_avg(3, order_dict)}')

'''
 How many unique customers did we have?
_________________________________________________________________________
Calculate the total number of unique customers in our sales data.

Then calculate the number of orders per customer (total orders / unique customers)
'''
total_orders = [order[0] for order in order_dict.values()]
total_orders_count = len([order[0] for order in order_dict.values()])
unique_customers = set([order[0] for order in order_dict.values()])
unique_customer_count = len(set([order[0] for order in order_dict.values()]))
# print(f"the number of orders per customer is: {total_orders_count / unique_customer_count}")

'''
 How many items in total did we sell?
____________________________________________________________________________
Calculate the total number of items we sold in across all orders. 

This information is in Column H, which should be the last element in 
order_dict's values.
'''
items_orders = [order[6] for order in order_dict.values()]
flat_orders = [item for items in items_orders for item in items]

# print(f"The total of items ordered is {len(flat_orders)}")

'''
 Sales By Location
___________________________________________________________________ 

Calculate the sum of subtotals by location.

Create a dictionary to store them, where location is the key, and 
revenue for that location is the value.

A few steps to consider:

* Loop through your dictionary
* build a dictionary as you go with location as key
* increment revenue every time a transaction matches the location.


Your output should look like 
{'Location1': sum of subtotals for 'Location1'}

With an entry for each location.
'''
location_sums = {}
for data in order_dict.values():
  location = data[5]
  if location not in location_sums:
    location_sums[location] = 0
  location_sums[location] += data[4]

# print(location_sums)

'''
 Challenge: Aggregator Function
_____________________________________________________________________
Now that you've summed revenue by category 
(you just summed by location), can you write a function to generalize 
calculating a sum of a column, grouped by the unique values in another 
column? (for example, sum of totals by date or customer_id).

Your function should take the following arguments:
* index of the 'column' (index position in order_dict) to group by
* index of the 'column' (index position in order_dict) to sum by category
* the dictionary where the data is located (assume the same structure as 
  order_dict.

It should return:
* A dictionary with the categories as keys, and the sum by category as value.

Once you've done so use your function to sum totals by date and customer_id.
'''

def aggregator(category_index, field_to_sum_index, dictionary):
  category_sums ={}
  for data in dictionary.values():
    category =  data[category_index]
    category_sums[category] = category_sums.get(category, 0) + data[field_to_sum_index]
  # print(category_sums)
  return category_sums

# print(aggregator(1, 4, order_dict))
  