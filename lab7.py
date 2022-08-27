print('\nЗадание 1:')


class Matrix:
    def __init__(self, my_matrix):
        self.my_matrix = my_matrix

    def __str__(self):
        return str('\n'.join([' '.join(map(str, row)) for row in self.my_matrix]))

    def __add__(self, other):
        for i in range(len(self.my_matrix)):
            for j in range(len(other.my_matrix[i])):
                self.my_matrix[i][j] = self.my_matrix[i][j] + other.my_matrix[i][j]
        return Matrix.__str__(self)


one_m = Matrix([[1, 2], [2, 3]])
two_m = Matrix([[4, 3], [3, 2]])
print(f'Первая матрица:\n{one_m}\n')
print(f'Вторая матрица:\n{two_m}\n')
print(f'Результат суммы матриц:\n{one_m + two_m}')


print('\nЗадание 2:')
from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def abstract(self):
        pass


class Coat(Clothes):

    def __init__(self, v):
        self.v = v

    @property
    def cost_cloth(self):
        return int(self.v / 6.5 + 0.5)

    def abstract(self):
        pass


class Costume(Clothes):

    def __init__(self, h):
        self.h = h

    @property
    def cost_cloth(self):
        return int(self.h * 2 + 0.3)

    def abstract(self):
        pass


a = Coat(50)
b = Costume(2)
print(f'Затраты ткани на пальто: {a.cost_cloth}')
print(f'Затраты ткани на костюм: {b.cost_cloth}')
print(f'Общие затраты ткани: {a.cost_cloth + b.cost_cloth}')


print('\nЗадание 3:')


class Cell:
    def __init__(self, num_cells):
        self.num_cells = int(num_cells)

    def __add__(self, other):
        return self.num_cells + other.num_cells

    def __sub__(self, other):
        sub_cells = self.num_cells - other.num_cells
        if sub_cells > 0:
            return sub_cells
        else:
            return f'Отрицательное кол-во клеток невозможно'

    def __mul__(self, other):
        return self.num_cells * other.num_cells

    def __truediv__(self, other):
        return self.num_cells // other.num_cells

    def make_order(self, cells_in_row):
        result = ''
        for i in range(self.num_cells // cells_in_row):
            result += '*' * cells_in_row + '\n'
        result += '*' * (self.num_cells % cells_in_row) + '\n'
        return result


c1 = Cell(11)
c2 = Cell(5)
print(c1 + c2)
print(c1 - c2)
print(c2 - c1)
print(c1 * c2)
print(c1 / c2)
print(c1.make_order(3))
