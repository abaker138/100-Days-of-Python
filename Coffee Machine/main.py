import menu

menu_list = menu.MENU
resources_list = menu.resources
cost = 0
transcating = True

def check_resources(resource_list, menu, menu_item):
    status = True
    item = menu[menu_item]
    ingredients = item["ingredients"]
    for n_item in ingredients:
        for n_resource in resource_list:
          if n_item == n_resource and resource_list[n_resource] > ingredients[n_item]:
            print("good to go")
            status = True
          elif n_item == n_resource and resource_list[n_resource] < ingredients[n_item]:
            status = False
            return status
    return status

def decrease_resources(resource_list, menu, menu_item):
  item = menu[menu_item]
  ingredients = item["ingredients"]
  for n_item in ingredients:
      for n_resource in resource_list:
        if n_item == n_resource:
          resource_list[n_item] -= ingredients[n_item]
  resource_list["money"] += item["cost"]
  print(resource_list)

while transcating:
  request = input("What drink would you like? Espresso, latte, or cappuccino?\n")
  if request in menu_list:
    good_to_go = check_resources(resources_list, menu_list, request)
    print(good_to_go)
    if good_to_go:
      cost = menu_list[request]["cost"]
      print(f"That will cost ${cost}, please")
    else:
      print("Sorry, we don't have enough ingredients for that.")
      break
    coins = {"quarters":int(input("How many quarters?: ")),
            "dimes":int(input("How many dimes?: ")),
            "nickels":int(input("How many nickels?: ")),
            "pennies":int(input("How many pennies?: "))}
    money = (coins["quarters"] * .25) + (coins["dimes"] * .10) + (coins["nickels"] * .05) + (coins["pennies"] * .01)
  
    if money > cost:
      difference = round(money - cost,2)
      print(f"Great, here is your {request}, and your change comes out to ${difference}. Have a great day!")
      decrease_resources(resources_list, menu_list, request)
  elif request == "report":
    print(resources_list)
