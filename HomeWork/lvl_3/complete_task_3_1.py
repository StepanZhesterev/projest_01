# -*- coding: utf-8 -*-
"""complete_task_3_1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ypWbngwcSSkrFivvpwCQ8iJz_kWhEqKN
"""
# Задача 3.1.
# Создайте класс матрицы (или таблицы).
# Требования к классу:
#   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
#   - в каждой ячейке содержится либо число, либо None
#   - доступы следующие методы матрицы:
#       * принимать новые значения, 
#       * заменять существующие значения, 
#       * выводить число строк и колонок.

# Пример матрицы 10 на 10 из единиц:
# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# Примечание! 
#   - новый класс не запрещено строить на базе существующих типов данных: списков, словарей и тд.
#   - отображать в таблице/матрице название колонки не обязательно!
#   - использовать готовые классы numpy.array() и pandas.DataFrame() запрещено!
#   - проявите фантазию :)
import random

class Matrix:

    def __init__(self, row, col):
        self.matrix = [[random.randrange(1, 10) for a in range(col)] for b in range(row)]
        self.row = row
        self.col = col

    def print(self):
      matrix = self.matrix
      for im in range(len(matrix)):
        print(matrix[im])

    def get(self):
      return [self.row, self.col]

    def showRaz(self):
        print('Размерность матрицы m = ', self.row, ', n = ', self.col)

    def changeByNumber(self):
      result = self.matrix
      for i in range(self.row):
        for j in range(self.col):
          if result[i][j] > 5:
            result[i][j] = random.randrange(11, 20)
      for im in range(len(result)):
        print(result[im])

    def obrat(self):
      matrix = self.matrix
      n = len(matrix)
      for i in range(n-1):
        for j in range(i+1,n):
          matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
      for im in range(len(matrix)):
        print(matrix[im])

    def changeByIndex(self):
      matrix = self.matrix
      user_input = input ('Сколько элементов вы хотите поменять в матрице? ')
      k =int(user_input)
      for k in range(k):
        user_input = input ('Введите номер строки элемента от 0 ')
        stroka = int(user_input)
        user_input = input ('Введите номер столбца элемента от 0 ')
        stolbets = int(user_input)
        matrix[stroka][stolbets] = random.randrange(21, 30)
      for im in range(len(matrix)):
        print(matrix[im])

    def changeMinOnMax(self):
      matrix =self.matrix
      imax = 0
      jmax = 0
      jmin = 0
      imin = 0
      maxmatrix = matrix[imax][jmax]
      minmatrix = matrix[imin][jmin]
      for i in range(self.row):
        for j in range(self.col):
          maxmatrix = matrix[imax][jmax]
          minmatrix = matrix[imin][jmin]
          if matrix[i][j] < minmatrix:
            jmin = j
            imin = i
          elif matrix[i][j] > maxmatrix:
            jmax = j
            imax = i
          matrix[imax][jmax], matrix[imin][jmin]  = matrix[imin][jmin], matrix[imax][jmax]
      for im in range(len(matrix)):
        print(matrix[im])


d = Matrix(10, 10)
print('Исходная матрица')
d1 = d.print()
print()
d.showRaz()
print('Изменненая матрица. Замена значений больше 5')
d2 = d.changeByNumber()
print('Обратная матрица')
d3 =d.obrat()
print('Изменная матрица. Замена по индексу')
d4 = d.changeByIndex()
print('Изменная матрица. Замена в 1 строке наименьшего значения с наибольшим')
d5 =d.changeMinOnMax()