def tax_calculator(subtotal, tax = .06):
  ''' takes in a subtotal and tax rate and returns [subtotal, tax, total]

  Args:
    subtotal (float or int): cost of item in transaction
    tax (float or optional): default tax rate is .06

  Returns:
    List: list containing subtotal, tax, and total
  
  '''
  print("Here's your total including the tax: ")
  return [subtotal, tax, (subtotal * (1 + tax))]

