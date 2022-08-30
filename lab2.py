print('Задание 1:')
spisok = [1, 3.12, 'slovo', True, None, (2, 3), [2, 3], {2, 3}]
for el in spisok:
    print(type(el))


print('\nЗадание 2:')
spisok = input('Введите значения через пробел: ').split(None) # Каждое значение заносим в список
for el in range(0, len(spisok) - 1, 2):
    spisok[el], spisok[el + 1] = spisok[el + 1], spisok[el] # Меняем рядом стоящие элементы местами
print(spisok)


print('\nЗадание 3:')
one_season = [12, 1, 2]
two_season = [3, 4, 5]
three_season = [6, 7, 8]
four_season = [9, 10, 11]
year = {'Зима': one_season, 'Весна': two_season, 'Лето': three_season, 'Осень': four_season} # заносим списки
a = int(input('Введите месяц: '))                                                            # в словарь
for el in year.keys():
    if a in year[el]:
        print(el)


print('\nЗадание 4:')
count = 1
stroka = input('Введите слова через пробел: ').split(None)
for el in stroka:
    print(count, el[:10:])
    count += 1


print('\nЗадание 5:')
my_list = [7, 5, 3, 3, 2]
a = int(input('Введите число: '))
for el in my_list:
    if a > el:
        my_list.insert(0, a)
        break
    elif a == el:
        my_list.insert(my_list.index(el), a)
        break
    elif min(my_list) > a:
        my_list.append(a)
        break
print(my_list)


print('\nЗадание 6:')
products = []
i = 1
n = int(input('Сколько товаров вы хотите добавить? '))
for el in range(0, n):
    user = input('Введите характеристики товара через пробел: ').split(None)
    products.append((i, {'Название': user[0], 'Цена': int(user[1]), 'Кол-во': int(user[2]), 'Единица измерения': user[3]}))
    i += 1
for el in products: # для вывода не в одну строку
    print(el)
analitic = {'Название': [], 'Цена': [], 'Кол-во': [], 'Единица измерения': []}
for el in products:
    analitic['Название'].append(el[1].get('Название'))
    analitic['Цена'].append(el[1].get('Цена'))
    analitic['Кол-во'].append(el[1].get('Кол-во'))
    analitic['Единица измерения'].append(el[1].get('Название'))
for key, el in analitic.items(): # для вывода не в одну строку
    print(key, el)
