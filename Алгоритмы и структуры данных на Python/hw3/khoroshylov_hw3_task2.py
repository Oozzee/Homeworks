# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

import random

SIZE = 20
MAX_LIMIT = 100
MIN_LIMIT = 0
array = [random.randint(MIN_LIMIT, MAX_LIMIT) for _ in range(SIZE)]
print(array)
array_even = []

for i in range(SIZE):
    if array[i] % 2 == 0:
        array_even.append(i)

print('Индексы четных элементов: ', end='')
for i in range(len(array_even)):
    print(array_even[i], end=' ')
