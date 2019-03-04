# 4. Определить, какое число в массиве встречается чаще всего.
import random

SIZE = 10
MAX_LIMIT = 10
MIN_LIMIT = 0
array = [random.randint(MIN_LIMIT, MAX_LIMIT) for _ in range(SIZE)]
print(f'Случайный массив: {array}')
num = 0
max_frq = 0

for i in range(SIZE):
    frq = 1
    for j in range(i + 1, SIZE):
        if array[i] == array[j]:
            frq += 1
    if frq > max_frq:
        max_frq = frq
        num = array[i]
print(f'Самое часто встречаемое число {num}, кол-во повторений: {max_frq}')
