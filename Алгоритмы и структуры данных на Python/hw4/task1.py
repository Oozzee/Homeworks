# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
# from random import random
import random
import cProfile

MAX_LIMIT = 1000
MIN_LIMIT = 0
min_num = 0
max_num = 0
spam = 0

# 1ый вариант

def first_var(n):
    min_num = 0
    max_num = 0
    array = [random.randint(MIN_LIMIT, MAX_LIMIT) for _ in range(n)]
    for i in range(n):
        if array[i] < array[min_num]:
            min_num = i
        elif array[i] > array[max_num]:
            max_num = i

    spam = array[max_num]
    array[max_num] = array[min_num]
    array[min_num] = spam

# "task1.first_var(100)"
# 100 loops, best of 5: 187 usec per loop



# # 2ой вариант

def second_var(n):
    array = [random.randint(MIN_LIMIT, MAX_LIMIT) for _ in range(n)]
    min_num = min(array)
    max_num = max(array)
    index_min_num = array.index(min_num)
    index_max_num = array.index(max_num)
    array[index_min_num],array[index_max_num] = array[index_max_num],array[index_min_num]

# "task1.second_var(100)"
# 100 loops, best of 5: 172 usec per loop

# 3ий вариант
#
def third_var(n):
    arr = [0] * n
    min_ = 0
    max_ = 0
    for i in range(n):
        arr[i] = int(random() * 100)
        if arr[i] > arr[max_]:
            max_ = i
        elif arr[i] < arr[min_]:
            min_ = i

# "task1.third_var(100)"
# 100 loops, best of 5: 49.2 usec per loop


#
# cProfile.run('first_var(100000)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.253    0.253 <string>:1(<module>)
#    100000    0.088    0.000    0.182    0.000 random.py:174(randrange)
#    100000    0.038    0.000    0.220    0.000 random.py:218(randint)
#    100000    0.068    0.000    0.093    0.000 random.py:224(_randbelow)
#         1    0.000    0.000    0.253    0.253 task1.py:14(first_var)
#         1    0.034    0.034    0.253    0.253 task1.py:15(<listcomp>)
#         1    0.000    0.000    0.253    0.253 {built-in method builtins.exec}
#    100000    0.007    0.000    0.007    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#    102254    0.018    0.000    0.018    0.000 {method 'getrandbits' of '_random.Random' objects}


# cProfile.run('second_var(100000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.001    0.001    0.257    0.257 <string>:1(<module>)
#    100000    0.087    0.000    0.179    0.000 random.py:174(randrange)
#    100000    0.038    0.000    0.217    0.000 random.py:218(randint)
#    100000    0.067    0.000    0.092    0.000 random.py:224(_randbelow)
#         1    0.000    0.000    0.255    0.255 task1.py:28(second_var)
#         1    0.034    0.034    0.251    0.251 task1.py:29(<listcomp>)
#         1    0.000    0.000    0.257    0.257 {built-in method builtins.exec}
#         1    0.003    0.003    0.003    0.003 {built-in method builtins.max}
#         1    0.002    0.002    0.002    0.002 {built-in method builtins.min}
#    100000    0.007    0.000    0.007    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#    102243    0.018    0.000    0.018    0.000 {method 'getrandbits' of '_random.Random' objects}
#         2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}


# cProfile.run('third_var(100000)')
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.065    0.065 <string>:1(<module>)
#         1    0.058    0.058    0.065    0.065 task1.py:38(third_var)
#         1    0.000    0.000    0.065    0.065 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#    100000    0.007    0.000    0.007    0.000 {method 'random' of '_random.Random' objects}


# Вывод: первый вариант самый долгий, т.к. все делается пошагово. Второй быстрее за счет функций min max, которые работает на СИ. Третий вариант оказался самым быстрым потому что сразу создает и сортирует числа.