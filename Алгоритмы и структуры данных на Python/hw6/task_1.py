# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
import  sys


summ_ = 0
n = int(input('Введите целое число: '))
summ_ += sys.getsizeof(n)
even = 0
odd = 0


while n > 0:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1
    n = n // 10

summ_ += sys.getsizeof(even)
summ_ += sys.getsizeof(odd)

print(f'В вашем числе {even} четных и {odd} нечетных чисел')

print(f'Было выделено {summ_} байт памяти.')
