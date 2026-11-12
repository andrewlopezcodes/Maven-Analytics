"""
#___________________________________________________________
 Improved Affordability Calculator.
#___________________________________________________________

We need to make sure our affordability calculator can handle 
many data types without stopping - our data is VERY messy. We 
need to make the following changes to the code below:


* Make sure it converts the string in the list below into a 
  float. Print a warning that this was string data. Then process
  as usual.

* Also, have the loop skip any instances of None data type.

* Then, remove the generic except statement to avoid processing 
  errors.

* Finally, change the hard coded value 50 into a variable so we
  can change this value based on each customer's budget.
"""

price_list = [5.99, None, 19.99, 24.99, 0, '74.99', 99.99]
budget = int(input("What is your budget: (please use an number)"))

# loop to calculate how many of each item I can buy
for price in price_list:
    try:
        if price == None:
                continue
        affordable_quantity = budget //price  # My budget is 50 dollars
        print(f"I can buy {affordable_quantity} of these.")
      
    except TypeError:
        print(f'string data detected at index {price_list.index(price)}')
        affordable_quantity = budget // float(price)
        print(f"I can buy {affordable_quantity} of these.")

    except ZeroDivisionError:
        print(f"This product at index {price_list.index(price)} is free, I can take as many as I like.")
    except:  # need to get rid of general except statement
        print('Thats not a number')