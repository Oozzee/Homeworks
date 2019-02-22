from random import random

print('\tЗадайте диапазон')
n1 = int(input('Введите начальное число: '))
n2 = int(input('Введите конечное число диапазона: '))
random_n = int(random() * (n2 - n1 + 1)) + n1
print(random_n)

print('\n\tЗадайте диапазон')
f1 = float(input('Введите начальное число: '))
f2 = float(input('Введите конечное число диапазона: '))
random_f = random() * (f2 - f1) + f1
print(round(random_f, 3))

print('\n\tЗадайте диапазон')
s1 = ord(input('Введите начальное символ: '))
s2 = ord(input('Введите конечный символ диапазона: '))
random_s = int(random() * (s2 - s1 + 1)) + s1
print(chr(random_s))
