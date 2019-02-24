a = 0
b = 0
a_max = 0
n_max = 0
while True:
    n = int(input('Введите число: '))
    if n != 0:
        a = 0
        b = n
        while n > 0:
            a = a + n % 10
            n = n // 10
        if a > a_max:
            a_max = a
            n_max = b
    else:
        break
print(f'Наибольшее число по сумме цифр {n_max}. Сумма его цифр равняется {a_max}.')
