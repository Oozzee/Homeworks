# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
import random

SIZE = 10
MAX_LIMIT = 100
MIN_LIMIT = 0
array = [random.randint(MIN_LIMIT, MAX_LIMIT) for _ in range(SIZE)]
print(f'Случайный массив: {array}')

max_num = 0
min_num = 0
total = 0
temp = 0

for i in range(SIZE):
    if array[i] < array[min_num]:
        min_num = i
    elif array[i] > array[max_num]:
        max_num = i

print(f'Наименьшее число: {array[min_num]}, наибольшее число: {array[max_num]}')

if min_num > max_num:
    for i in range(max_num + 1, min_num):
        total += array[i]
else:
    for i in range(min_num + 1, max_num):
        total += array[i]

print(f'Сумма элементов между самым маленьким и самым большим числом в массиве = {total}')

