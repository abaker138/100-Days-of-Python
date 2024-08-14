import menu

menu_list = menu.MENU
resources_list = menu.resources

request = input("What drink would you like? Espresso, latte, or cappuccino?\n")

def check_resources(resource_list, menu, menu_item):
    item = menu[menu_item]
    ingredients = item["ingredients"]
    for n in ingredients:
        print(ingredients[n])
    
check_resources(resources_list, menu_list, request)