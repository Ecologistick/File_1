from pprint import pprint
class CookBook(dict):
  def __init__(self, filename):
    with open(filename, encoding='utf-8') as file:
      onstring = file.read().splitlines()
    line = end = -1
    while line < len(onstring):
      item = onstring[line]
      if line < end:
        ingredient_name, quantity, measure = item.split(" | ")
        self[key].append(
          {"ingredient_name": ingredient_name, "quantity": int(quantity), "measure": measure}
        )
        line += 1
      else:
        key = onstring[line + 1]
        self[key] = []
        end = line + 3 + int(onstring[line + 2])
        line += 3

  def get_shop_list_by_dishes(self, dishes, person_count):
    shop_list = {}
    for dish in dishes:
      for ingredient in cook_book[dish]:
        ingredient_name = ingredient["ingredient_name"]
        if ingredient_name not in shop_list:
          shop_list[ingredient_name] = {
            "measure": ingredient["measure"], "quantity": ingredient["quantity"] * person_count
          }
        else:
          shop_list[ingredient_name]["quantity"] += ingredient["quantity"] * person_count
    return shop_list

cook_book = CookBook('recipes.txt')
pprint(cook_book.get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
