print('\nЗадание 1:')
# запуск задания осуществляется через терминал с параметрами
from sys import argv

script_name, work_hour, cost_hour, bonus = argv
print('Ваша зарплата составит: ', (int(work_hour) * int(cost_hour)) + int(bonus))


print('\nЗадание 2:')
spisok = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_spisok = [spisok[el+1] for el in range(len(spisok)-1) if spisok[el] < spisok[el+1]]
print(new_spisok)


print('\nЗадание 3:')
spisok = [el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]
print(spisok)


print('\nЗадание 4:')
spisok = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_spisok = [el for el in spisok if spisok.count(el) == 1]
print(new_spisok)


print('\nЗадание 5:')
from functools import reduce
def my_func(prev_el, el):
    return prev_el * el

print(reduce(my_func, range(100, 1001, 2)))


print('\nЗадание 6:')
from itertools import count, cycle
n = int(input("Введите целое число:"))

for i in count(n):
    if i <= 100:
        print(i)

spisok = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
counter = 0
for el in cycle(spisok):
    if counter <= 100:
        print(el)
        counter += 1


print('\nЗадание 7:')
from math import factorial
def fact(el):
    yield factorial(el)

a = int(input('Введите число: '))
for el in fact(a):
    print(el)
