'''
 New Currency Prices
______________________________________________________________
Hi there, we need to add British Pound and Japanese Yen pricing 
to our 'Item_Info' sheet in the Maven data Excel workbook.

I've included the code to read in the excel workbook below.
'''
import openpyxl as xl
import currency_converter as cc

wb = xl.load_workbook(filename='maven_ski_shop_data.xlsx')

items = wb['Item_Info']

'''
 Currency Converter
______________________________________________________________
Since we're going to be doing this a few times 
(and hopefully more in the future), let's create a 
currency_converter function to take a price, and an exchange 
rate, returning a converted price rounded to two decimal places.

'''
# def currencyConverter(x):
#   pound_exchange_rate = .76
#   yen_exchange_rate = 123
#   euro_exchange_rate =  .879
#   euro =  round(x * euro_exchange_rate, 2)
#   yen  =  round(x * yen_exchange_rate, 2)
#   pound=  round(x * pound_exchange_rate, 2)
  
#   euro_symbol = "£"
#   yen_symbol =  "¥"
#   pound_symbol ="£"

#   print(f'the converted currency for ${x} is Euro: {euro_symbol}{euro} GB Pound: {pound_symbol}{pound} Yen: {yen_symbol}{yen}')
#   return [euro, pound, yen]

def currency_converter(price, rate):
  currency = float(price)
  conversion = float(rate)
  return round(currency * conversion, 2)

'''
 British Pound Column
_______________________________________________________________
Now that we have a currency converter, create a column with 
British Pound prices, in the column to the right of the 
Euro prices.

Don't forget to add a column title - 'GBP Price' Should Work!
'''

pound_exchange_rate = 0.76

items["G1"] = "GBP Price"
print(items["G1"].value)

for row in range(2, items.max_row + 1):
  items[f"G{row}"] = currency_converter(items[f"C{row}"].value, pound_exchange_rate)
  print(F"G{row}", items[f"G{row}"].value)


'''
 Japanese Yen Column
________________________________________________________________
Next, create a Japanese Yen Column with the same method we did 
for British Pounds.

Call this column 'JPY Price'
'''

yen_exchange_rate = 123

for index, cell in enumerate(items['C'], start= 1):
  if index == 1:
    items[f'H{index}'] = 'JPY Price'
  else:
    items[f'H{index}'] = currency_converter(cell.value, yen_exchange_rate)
    print(f"H{index}", cell.value)


'''
 Save your work!
________________________________________________________________
Finally, save your workbook as 'maven_data_new_pricing.xlsx'.

We'll cover this soon - just run the cell below, and check your 
notebook folder for a .xlsx file.
'''

wb.save(filename='maven_data_new_pricing.xlsx')