def whatFlavors(cost, money):
  cost_id_dict = {}
  for i, price in enumerate(cost):
    if money-price in cost_id_dict:
      print(str(cost_id_dict[money-price]+1) + " " + str(i+1))
    else:
      cost_id_dict[price] = i