def currencyConverter(x):
  currency = float(x)
  pound_exchange_rate = .76
  yen_exchange_rate = 123
  euro_exchange_rate = .879
  euro =  round(currency * euro_exchange_rate, 2)
  yen  =  round(currency * yen_exchange_rate, 2)
  pound=  round(currency * pound_exchange_rate, 2)
  
  euro_symbol = "£"
  yen_symbol =  "¥"
  pound_symbol ="£"

  print(f'the converted currency for ${x} is Euro: {euro_symbol}{euro} GB Pound: {pound_symbol}{pound} Yen: {yen_symbol}{yen}')
  return [euro, pound, yen]


