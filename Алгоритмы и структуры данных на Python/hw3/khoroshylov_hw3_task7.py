# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
import random

SIZE = 10
MAX_LIMIT = 10
MIN_LIMIT = 0
array = [random.randint(MIN_LIMIT, MAX_LIMIT) for _ in range(SIZE)]
print(f'Случайный массив: {array}')

if array[0] > array[1]:
    min1 = 0
    min2 = 1
else:
    min1 = 1
    min2 = 0

for i in range(2, SIZE):
    if array[i] < array[min1]:
        b = min1
        min1 = i
        if array[b] < array[min2]:
            min2 = b
    elif array[i] < array[min2]:
        min2 = i

print(f'Первое минимальное число: {array[min1]}, второе минимальное число: {array[min2]}')
