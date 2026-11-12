import openpyxl as xl

workbook = xl.load_workbook(filename='maven_ski_shop_data.xlsx')
workbook.active = 1
items = workbook['Item_Info']
inventory = workbook['Inventory_Levels']
orders = workbook['Orders_Info']

wb = xl.load_workbook(filename='maven_ski_shop_data.xlsx')
inventory =wb['Inventory_Levels']

for i, cell in enumerate(inventory['B'], start = 1):  # i = index, in the Workbook named inventory iterate over each cell in column B starting with B1
  if i == 1:                                          #   if index is exactly 1
    inventory[f'C{i}'] = 'Inventory Status'           #     in the workbook named inventory in column C with row of index == 1 write "Inventory Status"
  elif cell.value > 5:                                #   else if in column B with row matching index i read the cell value, if it is greater than 5
    inventory[f'C{i}'] = 'Healthy Stock'              #     in the workbook named inventory in column C with row of index matching i write "Healthy Stock"
  elif cell.value > 0:                                #   else if in column B with row matching index i read the cell value, if it is greater than 0
    inventory[f'C{i}'] = 'Low Stock'                  #     in the workbook named inventory in column C with row of index matching i write "Low Stock"
  else:                                               #   else if in column B with row matching index i read the cell value, if it is less than or equal to 0 
    inventory[f'C{i}'] = 'Out of Stock'               #     in the workbook named inventory in column C with row of index matching i write "Out of Stock"
  print(f'C{i}', inventory[f'C{i}'].value)            #   print column C index matching i , in the workbook named inventory read and return the value of column C index matching i


  wb.save('maven_ski_shop_inventory_fix.xlsx')