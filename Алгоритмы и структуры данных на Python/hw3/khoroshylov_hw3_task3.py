# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

SIZE = 10
MAX_LIMIT = 100
MIN_LIMIT = 0
array = [random.randint(MIN_LIMIT, MAX_LIMIT) for _ in range(SIZE)]
print(f'Случайный массив: {array}')
max_num = 0
min_num = 0
temp = 0

for i in range(SIZE):
    if array[i] < array[min_num]:
        min_num = i
    elif array[i] > array[max_num]:
        max_num = i

print(f'\nМаксимальное число: {array[max_num]}')
print(f'Минимальное число: {array[min_num]}')

temp = array[max_num]
array[max_num] = array[min_num]
array[min_num] = temp

print(f'\nЗамена мест максимального и минимального элементов: {array}')


