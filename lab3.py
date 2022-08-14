print('Задание 1:')
def divide(arg_1, arg_2):
    return None if arg_2 == 0 else arg_1 / arg_2

a = int(input('Введите делимое: '))
b = int(input('Введите делитель: '))
print(divide(a, b))


print('\nЗадание 2:')
# Аргументы перепутаны местами для демонстрации работы именованных аргументов
def person (first_name, second_name, age, city, mail, number):
    return print(f'{first_name} {second_name} {age} {city} {mail} {number}')

print(person(second_name = input('Введите фамилию: '),
             first_name = input('Введите имя: '),
             mail = input('Введите email: '),
             number = input('Введите номер телефона: '),
             age = int(input('Введите год рождения: ')),
             city = input('Введите город проживания: ')))


print('\nЗадание 3:')
def my_func(a, b, c):
    if a <= b and a <= c:
        return b + c
    elif b <= a and b <= c:
        return a + c
    elif c <= a and c <= b:
        return a + b

one_var = int(input('Введите первое значение: '))
two_var = int(input('Введите второе значение: '))
three_var = int(input('Введите третье значение: '))
print(f'Сумма двух наибольших чисел: {my_func(one_var, two_var, three_var)}')


print('\nЗадание 4:')
def my_func(x, y):
    return x ** y
# Второй способ решения задачи через цикл
def my_func(x, y):
    new_var = x
    for el in range(-1, y, -1):
        while el >= y:
            new_var = new_var * x
            break
    return 1 / new_var

while True:
    one_var = float(input('Введите действительное положительное число: '))
    if one_var >= 0:
        x = one_var
        break
    else:
        print('Введите положительное число!')
while True:
    two_var = int(input('Введите целое отрицательное число: '))
    if two_var < 0:
        y = two_var
        break
    else:
        print('Введите отрицательное число!')
print(my_func(x, y))


print('\nЗадание 5:')
summa = 0
def summ(args):
    global summa, flag
    flag = False
    for el in args:
        try:
            if el:
                summa += el
        except TypeError:
            flag = True
    return summa, flag

while True:
    spisok = input('Введите числа через пробел: ').split(' ')
    x = 0
    for el in spisok:
        if el != '/':
            spisok[x] = int(spisok[x])
            x += 1
    summa, flag = summ(spisok)
    print(summa)
    if flag:
        break


print('\nЗадание 6 и 7:')
def int_func(args):
    new_spisok = args.title()
    return new_spisok

spisok = input('Введите слова в нижнем регистре через пробел: ')
print(int_func(spisok))
