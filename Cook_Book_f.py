def file_write(file_name: str, mode: str, data=''):
  with open(file_name, mode) as file:
    file.write(f"{data}\n")

def isdig(data):
  try:
    int(data)
    return True
  except ValueError:
    return False

def file_read(name_file):
  cook_book = {}
  with open(name_file, 'r') as file:
    for line in file:
      if len(line.split(' | ')) == 1 and isdig(line) == False and len(line) >= 2:
        name_food = line.strip(' \n')
        cook_book[name_food] = []
      if len(line.split(' | ')) == 3 and len(line) > 2:
        ingred_dict = {}
        ingr_list = line.split(' | ')
        ingred_dict['ingredient_name'] = ingr_list[0]
        ingred_dict['quantity'] = ingr_list[1]
        ingred_dict['measure'] = ingr_list[2].strip(' \n')
        cook_book[name_food].append(ingred_dict)
  return cook_book

def file_save(name_file):
  for name_food, ingred_list in cook_book.items():
    text = f'\n{name_food} \n{len(ingred_list)}'
    file_write(name_file, 'a', text)
    for ingred_food in ingred_list:
      text = f"{ingred_food.get('ingredient_name')} | {ingred_food.get('quantity')} | {ingred_food.get('measure')}"
      file_write(name_file, 'a', text)

def list_food():
  n_food = input("Введите название блюда: ").capitalize()
  print(n_food)
  n = 0
  for i in cook_book[n_food]:
    print(i)
    n +=1
  print(n)

def list_food_dict():
  for food in cook_book.keys():
    print(food)

def get_shop_list_by_dishes(dishes, person_count):
  shop_dict = {}
  for dish in dishes:
    if dish in cook_book.keys():
      for ingred_dict in cook_book[dish]:
        if ingred_dict['ingredient_name'] not in shop_dict:
          shop_dict[ingred_dict['ingredient_name']] = \
            {'measure': ingred_dict['measure'], 'quantity': int(ingred_dict['quantity'])*person_count}
        else:
          # добавляем кол-во текущего ингридиента к кол-вy ингр в уже созданном словаре по данному продукту
          # int(ingred_dict['quantity'])*person_count + (shop_dict[ingred_dict['ingredient_name']]['quantity'])
          shop_dict[ingred_dict['ingredient_name']] = \
            {'measure': ingred_dict['measure'],
             'quantity': int(ingred_dict['quantity'])*person_count + shop_dict[ingred_dict['ingredient_name']]['quantity']}

    else:
      print(f"Запрошенное блюдо {dish} отсутствует в книге рецептов")
  return shop_dict


cook_book = file_read('CookBook.txt')
# list_food_dict()
print(get_shop_list_by_dishes(['Салат', 'Суп куриный'], 3))
# for ingr_n, q in get_shop_list_by_dishes(['Салат', 'Суп куриный'], 3).items():
#   print(f"{ingr_n},{q}")

