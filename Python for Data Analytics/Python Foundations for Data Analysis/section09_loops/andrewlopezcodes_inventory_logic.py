"""
#___________________________________________________________________________
Calculate Projected Inventory for Each Month
#___________________________________________________________________________

We currently have 686 pairs of skis in inventory, and sell 84 each month.

Write a program that keeps track of monthly inventory, by subtracting 84 
pairs of skis from inventory each month. 

Your program should print 'At the end of month x, we have y pairs of inventory', 
where x is the number of months that has gone by and y is the remaining inventory 
at that month.

If inventory goes negative, your program should stop running.

"""


current_inventory = 686
monthly_sales = 84
month = 0

while current_inventory > 0:
  current_inventory -= monthly_sales
  month += 1
  print(f"At the end of month {month}, we have {current_inventory} pairs of skis")