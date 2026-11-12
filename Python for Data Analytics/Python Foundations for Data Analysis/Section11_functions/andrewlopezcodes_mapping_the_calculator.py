'''
 Mapping the tax calculator
___________________________________________________ 

Now that we've successfully got our tax calculator 
working, can you apply it to the subtotals below?

Should be quick! Thanks!

P.S. Don't use a loop!
'''
import tax_calculator as tc

subtotals = [1799.94, 99.99, 254.95, 29.98, 99.99]

print(list(map(tc.tax_calculator, subtotals)))