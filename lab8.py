print('\nЗадание 1:')


class Data:
    def __init__(self, dmy):
        self.dmy = dmy

    @classmethod
    def revers(cls, dmy):
        dmy = dmy.split('-')
        return list(map(int, dmy))

    @staticmethod
    def valid(dmy):
        day, month, year = Data.revers(dmy)
        if year <= 0:
            return False
        if month <= 0 or month > 12:
            return False
        if day <= 0 or day > 31:
            return False
        if month in [4, 6, 9, 11] and day == 31:
            return False
        if month == 2 and day > 28 and year % 4 != 0:
            return False
        elif month == 2 and day > 29 and year % 4 == 0:
            return False
        return True


print(Data.revers('10-02-2022'))
print(Data.valid('29-02-2020'))


print('\nЗадание 2:')


class CustomError(Exception):
    def __init__(self, txt_err):
        self.txt_err = txt_err


while True:
    try:
        a = int(input('Введите делимое: '))
        b = int(input('Введите делитель: '))
        if b == 0:
            raise CustomError('На ноль делить нельзя!')
        else:
            print(a / b)
            continue
    except CustomError as err:
        print(err)
        continue


print('\nЗадание 3:')


class CustomError(Exception):
    def __init__(self, txt_err):
        self.txt_err = txt_err

result = []
while True:
    try:
        num = input('Введите число или stop для выхода: ')
        if num == 'stop':
            break
        elif not num.isdigit():
            raise CustomError('Вы ввели не число!')
        else:
            result.append(num)
            continue
    except CustomError as err:
        print(err)
        continue
print(result)


print('\nЗадание 4-6:')


class StokOffTech:
    @staticmethod
    def empty():
        pass


class OffTech:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.items = {}

    def valid(self):
        try:
            name = input('Введите название: ')
            quantity = int(input('Введите кол-во устройств: '))
            price = int(input('Введите стоимость одного устройства: '))
            item = {'Название': name, 'Цена': price, 'Количество': quantity}
            self.items.update(item)
        except ValueError:
            print('Вы ввели недопустимое значение')


class Printer(OffTech):
    def __init__(self, name, price, quantity, color):
        super().__init__(name, price, quantity)
        self.color = color


class Scanner(OffTech):
    def __init__(self, name, price, quantity, scan_speed):
        super().__init__(name, price, quantity)
        self.scan_speed = scan_speed


class Copier(OffTech):
    def __init__(self, name, price, quantity, color, scan_speed):
        super().__init__(name, price, quantity)
        self.color = color
        self.scan_speed = scan_speed


p = Printer('HP', 1500, 5, 'RGB')
s = Scanner('Scr', 1000, 10, 5)
c = Copier('Xerox', 2500, 30, 'Black', 3)

p.valid()
s.valid()
c.valid()

print(p.items)
print(s.items)
print(c.items)


print('\nЗадание 7:')


class ComplexNum:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __add__(self, other):
        return f'Сумма равна: {self.real + other.real} + i * {self.img + other.img}'

    def __mul__(self, other):
        return f'Произведение равно: {self.real * other.real - self.img * other.img} +' \
               f' i * {self.real * other.img + self.img * other.real}'


c_1 = ComplexNum(4, -8)
c_2 = ComplexNum(6, 11)
print(c_1 + c_2)
print(c_1 * c_2)



