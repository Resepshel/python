print('\nЗадание 1:')
text = input('Введите текст: ')
with open('text.txt', 'w+') as f_obj:
    while text:
        f_obj.writelines(text + '\n')
        text = input('Введите текст: ')
        if text == '':
            break
    f_obj.seek(0)
    text_in_file = f_obj.read()
    print(text_in_file)


print('\nЗадание 2:')
with open('text.txt') as f_obj:
    strok = len(f_obj.readlines())
    print(f'Кол-во строк в файле: {strok}')
    f_obj.seek(0)
    slov = f_obj.read()
    slov = slov.split()
    print(f'Кол-во слов в файле: {len(slov)}')


print('\nЗадание 3:')
summa = []
print('Список сотрудников, чей оклад меньше 20000:')
with open('zp.txt') as f_obj:
    price = f_obj.read()
    price = price.split('\n')
    for el in price:
        el = el.split()
        if int(el[1]) < 20000:
            print(el[0])
        summa.append(int(el[1]))
    f_obj.seek(0)
    print(f'\nСредняя величина дохода сотрудников: {(sum(summa) / len(f_obj.readlines())):.3f}')


print('\nЗадание 4:')
new_rus = []
rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('numbers.txt') as f_obj:
    for el in f_obj:
        el = el.split()
        new_rus.append(f'{rus[el[0]]} - {el[2]}\n')
    print(new_rus)

    with open('new_numders.txt', 'w', encoding='utf8') as new_f_obj:
        new_f_obj.writelines(new_rus)


print('\nЗадание 5:')
summa = 0
with open('text.txt', 'w+') as f_obj:
    f_obj.write(input('Введите числа через пробел: '))
    f_obj.seek(0)
    revers = f_obj.read().split(' ')
    revers = [int(el) for el in revers]
    for el in range(0, len(revers)):
        summa = summa + revers[el]
    print(f'Сумма всех чисел в файле: {b}')


print('\nЗадание 6:')
uni_dict = {}
with open('university.txt', 'r', encoding='utf8') as f_obj:
    rf = f_obj.readlines()
    for el in rf:
        revers = el.split()
        hour_sum = 0
        for h in revers[1:]:
            hour_sum += int(h.split('(')[0])
        uni_dict[revers[0]] = hour_sum
    print(uni_dict)


print('\nЗадание 7:')
import json
with open('firms.txt', 'r', encoding='utf8') as f_obj:
    gen_profit = 0
    average_profit = 0
    counter = 0
    stat = {}
    full_stat = []
    lines = f_obj.readlines()
    for el in lines:
        name, form, earning, cost = el.split()
        profit = int(earning) - int(cost)
        if profit >= 0:
            gen_profit += profit
            counter += 1
        stat[name] = profit
    if counter > 0:
        average_profit = gen_profit / counter
    full_stat.append(stat)
    full_stat.append({'average_profit': average_profit})
with open('firms.json', 'w', encoding='utf8') as json_file:
    json.dump(full_stat, json_file)
