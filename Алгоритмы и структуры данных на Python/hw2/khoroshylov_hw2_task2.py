n = int(input('Введите целое число: '))
even = 0
odd = 0

while n > 0:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1
    n = n // 10
print(f'В вашем числе {even} четных и {odd} нечетных чисел')
