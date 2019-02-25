a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

if a < b < c or c < b < a:
    print(f'{b} среднее число')
elif c < a < b or b < a < c:
    print(f'{a} среднее число')
else:
    print(f'{c} среднее число')
