"""
Лабораторна робота №23
ІПЗ - 12, Петраківський Данило
"""
from struct import unpack, pack
from math import sqrt
from os import stat
from random import uniform

buffer = 4


def get_element_1():
    """
    #1
    """
    i = int(input('Введіть i: ')) - 1
    j = int(input('Введіть j: ')) - 1
    filename = input('Введіть ім\'я файлу: ')
    with open(filename, 'rb') as file:
        file.seek((i * unpack('i', file.read(buffer))[0] + j) * buffer, 1)
        print(unpack('f', file.read(buffer))[0])


def get_element_2():

    """
    #2
    """
    i = int(input('Введіть i: ')) - 1
    j = int(input('Введіть j: ')) - 1
    filename = input('Введіть ім\'я файлу: ')
    with open(filename, 'rb') as file:
        file.seek((i * get_square_matrix_size(filename) + j) * buffer)
        print(unpack('f', file.read(buffer))[0])


def get_square_matrix_size(filename):
    return int(sqrt(stat(filename).st_size / buffer))


# noinspection PyUnusedLocal
def transpose_matrix():
    """
    #3
    """
    filename = input('Введіть ім\'я файлу: ')
    with open(filename, 'r+b') as file:
        m = get_square_matrix_size(filename)
        matrix = [[file.read(buffer) for j in range(m)] for i in range(m)]
        clear(file)
        for i in range(m):
            for j in range(m):
                file.write(matrix[j][i])


def clear(file):
    file.seek(0)
    file.truncate()


def add_matrices():
    """
    #4
    """
    combine(input('Введіть ім\'я 1 файлу: '), input('Введіть ім\'я 2 файлу: '),
            input('Введіть ім\'я 3 файлу: '), lambda x, y: x + y)


def combine(filename_1, filename_2, filename_3, combiner):
    with open(filename_1, 'rb') as file_1, open(filename_2, 'rb') as file_2, open(filename_3, 'wb') as file_3:
        for i in range(0, stat(filename_1).st_size, buffer):
            file_3.write(pack('f', combiner(unpack('f', file_1.read(buffer))[0], unpack('f', file_2.read(buffer))[0])))


def subtract_matrices():
    """
    #5
    """
    combine(input('Введіть ім\'я 1 файлу: '), input('Введіть ім\'я 2 файлу: '),
            input('Введіть ім\'я 3 файлу: '), lambda x, y: x - y)


def multiply_matrices():
    """
    #6
    """
    filename_1 = input('Введіть ім\'я 1 файлу: ')
    filename_2 = input('Введіть ім\'я 2 файлу: ')
    filename_3 = input('Введіть ім\'я 3 файлу: ')
    with open(filename_1, 'rb') as file_1, open(filename_2, 'rb') as file_2, open(filename_3, 'wb') as file_3:
        m = get_square_matrix_size(filename_1)
        matrix_1 = [[unpack('f', file_1.read(buffer))[0] for j in range(m)] for i in range(m)]
        matrix_2 = [[unpack('f', file_2.read(buffer))[0] for j in range(m)] for i in range(m)]
        for i in range(m):
            for j in range(m):
                element = 0
                for k in range(m):
                    element += matrix_1[i][k] * matrix_2[k][j]
                file_3.write(pack('f', element))


def create_matrix(filename):
    with open(filename, 'wb') as file:
        matrix = [[-1, 2, -5], [3, 4, 1], [0, 1, 2]]
        for i in range(3):
            for j in range(3):
                file.write(pack('f', matrix[i][j]))


create_matrix('res/matrix1')
create_matrix('res/matrix2')
multiply_matrices()
with open('res/matrix', 'rb') as file:
    m = get_square_matrix_size('res/matrix')
    for i in range(m):
        for j in range(m):
            print(unpack('f', file.read(buffer))[0], end=' ')
        print()