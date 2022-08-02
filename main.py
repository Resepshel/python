print('Задание 1:')
a = input('Введите слово: ')
b = int(input('Введите число: '))
c = float(input('Введите дробь: '))
print(a)
print(b)
print(c)


print('\nЗадание 2:')
a = int(input('Введите время в секундах: '))
b = int(a / 60)
c = int(b / 60)
print(f'{c}:{b % 60}:{a % 60}')


print('\nЗадание 3:')
a = int(input('Введите число: '))
summa = int(str(a) + str(a) + str(a)) + int(str(a) + str(a)) + a # aaa + aa + a
print(summa)


print('\nЗадание 4:')
a = int(input('Введите целое положительное число: '))
z = -1
while a >= 1:
    b = a
    a = a // 10
    if b % 10 > z:
        z = b % 10
    if b > 9:       # для проверки первой цифры в числе
        continue
    else:
        print(z)
        break
print(z)


print('\nЗадание 5 и 6:')
a = int(input('Введите значение выручки: '))
b = int(input('Введите значение издержек: '))
c = -1
if a > b:
    c = a - b
    print(f'Ваша прибыль составляет: {c}')
    print(f'Рентабельность выручки составляет: {c / a:.3f}')
    e = int(input('Введите число сотрудников: '))
    print(f'Прибыль в расчёте на 1 сотрудника: {c / e:.3f}')
elif a < b:
    c = b - a
    print(f'Ваши убытки составляют: {c}')
else:
    print('Вы ничего не заработали, но и не потеряли')


print('\nЗадание 7:')
a = int(input('Введите кол-во км в первый день: '))
b = int(input('Введите кол-во км которые желаете достичь: '))
d = 0
while a < b:
    d = d + 1
    a = (a / 10) + a
    continue
d = d + 1
print(f'На {d} день вы выполните цель')