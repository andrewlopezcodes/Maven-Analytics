'''
 Excel Data Sales Tax
________________________________________________________
We need to calculate the sales tax for customer C00010 
in the excel workbook 'maven_ski_shop_data'.

Their transaction should be in row 'D10'. 
Apply a sales tax of 8%. 

First:

* Import the openpyxl library.
* Then load the workbook 'maven_ski_shop_data.xlsx' into Python (this is in the current section folder).
* Finally, assign a name to the 'Orders_Info' worksheet.
'''

import openpyxl as xl
import tax_calculator as tc

workbook = xl.load_workbook(filename='maven_ski_shop_data.xlsx')

orders = workbook['Orders_Info']

'''
 Sales Tax Calculation
_______________________________________________________ 

Ok, you should be ready to go - calculate the sales tax 
and total for the transaction in cell D10. 

Remember we already have a tax calculator function to do 
this! 

Consider printing your output with a string message!
'''
print(orders["D10"].value)

print(f"The taxes for this order are: ${tc.tax_calculator(orders['D10'].value, .08)[1]}.\nThe total for this order is: ${tc.tax_calculator(orders['D10'].value, .08)[2]}")
