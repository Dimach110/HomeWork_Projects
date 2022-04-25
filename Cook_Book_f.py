def file_write(file_name: str, mode: str, data=''):
  with open(file_name, mode) as file:
    file.write(f"{data}\n")

def file_save(file_name: str, mode: str='w', data=''):
  with open(file_name, mode) as file:
    file.write(data)

def isdig(data):
  try:
    int(data)
    return True
  except ValueError:
    return False

# cook_book = {
#   'Каша овсяная': [
#     {'ingredient_name': 'Овсяные хлопья', 'quantity': 3, 'measure': 'ст.л.'},
#     {'ingredient_name': 'Молоко', 'quantity': 50, 'measure': 'мл.'},
#     {'ingredient_name': 'Сахар', 'quantity': 2, 'measure': 'ч.л.'}
#     ],
#   'Суп куриный': [
#     {'ingredient_name': 'Куриное бедро', 'quantity': 1, 'measure': 'шт.'},
#     {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л.'},
#     {'ingredient_name': 'Лук', 'quantity': 1, 'measure': 'шт.'},
#     {'ingredient_name': 'Морковь', 'quantity': 1, 'measure': 'шт.'},
#     {'ingredient_name': 'Картофель', 'quantity': 2, 'measure': 'шт.'},
#     {'ingredient_name': 'Соль', 'quantity': 1, 'measure': 'ч.л.'}
#     ],
#   'Запеченный картофель': [
#     {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг.'},
#     {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч.'},
#     {'ingredient_name': 'Сыр', 'quantity': 100, 'measure': 'г.'},
#     ],
#   'Салат': [
#     {'ingredient_name': 'Картофель', 'quantity': 3, 'measure': 'шт.'},
#     {'ingredient_name': 'Морковь', 'quantity': 2, 'measure': 'л.'},
#     {'ingredient_name': 'Лук', 'quantity': 1, 'measure': 'шт.'},
#     {'ingredient_name': 'Колбаса', 'quantity': 300, 'measure': 'гр.'},
#     {'ingredient_name': 'Горошек', 'quantity': 1, 'measure': 'банка'},
#     {'ingredient_name': 'Огурец', 'quantity': 1, 'measure': 'шт.'},
#     {'ingredient_name': 'Яйцо', 'quantity': 3, 'measure': 'шт.'},
#     {'ingredient_name': 'Майонез', 'quantity': 3, 'measure': 'ст.л.'},
#     {'ingredient_name': 'Соль', 'quantity': 1, 'measure': 'ч.л.'}
#     ]
#   }
#
def file_save(name_file)
  for name_food, ingred_list in cook_book.items():
    text = f'\n{name_food} \n{len(ingred_list)}'
    file_write(name_file, 'a', text)
    for ingred_food in ingred_list:
      text = f"{ingred_food.get('ingredient_name')} | {ingred_food.get('quantity')} | {ingred_food.get('measure')}"
      file_write(name_file, 'a', text)

# with open('CookBook_save.txt', "w") as file:
#   file.write(f'{cook_book}')

def read_file(name_file):
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


# for food, ingr in cook_book.items():
#   print(food)
#   for ingr_l1 in ingr:
#     print(ingr_l1)

# {'Каша овсяная': [
#   {'ingredient_name': 'Овсяные хлопья', 'quantity': '3', 'measure': 'ст.л.'},
#   {'ingredient_name': 'Молоко', 'quantity': '50', 'measure': 'мл.'},
#   {'ingredient_name': 'Сахар', 'quantity': '2', 'measure': 'ч.л.'}],
# 'Суп куриный': [
#   {'ingredient_name': 'Куриное бедро', 'quantity': '1', 'measure': 'шт.'},
#   {'ingredient_name': 'Вода', 'quantity': '2', 'measure': 'л.'},
#   {'ingredient_name': 'Лук', 'quantity': '1', 'measure': 'шт.'},
#   {'ingredient_name': 'Морковь', 'quantity': '1', 'measure': 'шт.'},
#   {'ingredient_name': 'Картофель', 'quantity': '2', 'measure': 'шт.'},
#   {'ingredient_name': 'Соль', 'quantity': '1', 'measure': 'ч.л.'}],
# 'Запеченный картофель': [
#   {'ingredient_name': 'Картофель', 'quantity': '1', 'measure': 'кг.'},
#   {'ingredient_name': 'Чеснок', 'quantity': '3', 'measure': 'зубч.'},
#   {'ingredient_name': 'Сыр', 'quantity': '100', 'measure': 'г.'}],
# 'Салат': [
#   {'ingredient_name': 'Картофель', 'quantity': '3', 'measure': 'шт.'},
#   {'ingredient_name': 'Морковь', 'quantity': '2', 'measure': 'л.'},
#   {'ingredient_name': 'Лук', 'quantity': '1', 'measure': 'шт.'},
#   {'ingredient_name': 'Колбаса', 'quantity': '300', 'measure': 'гр.'},
#   {'ingredient_name': 'Горошек', 'quantity': '1', 'measure': 'банка'},
#   {'ingredient_name': 'Огурец', 'quantity': '1', 'measure': 'шт.'},
#   {'ingredient_name': 'Яйцо', 'quantity': '3', 'measure': 'шт.'},
#   {'ingredient_name': 'Майонез', 'quantity': '3', 'measure': 'ст.л.'},
#   {'ingredient_name': 'Соль', 'quantity': '1', 'measure': 'ч.л.'}
#   ]
# }
#
n_food = "Суп куриный"
print(n_food)
n = 0
for i in cook_book[n_food]:
  print(i)
  n +=1
print(n)