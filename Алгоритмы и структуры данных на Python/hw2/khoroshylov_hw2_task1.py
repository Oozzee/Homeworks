print('Программа поможет Вам выполнить простейшие математические операции( + - * /).\nДля выхода введите ноль.')
while True:
    s = input('Введите знак операции: ')
    if s == '0':
        break
    if s in ('+', '-', '*', '/'):
        x = float(input('Введите число Х: '))
        y = float(input('Введите число Y: '))
        if s == '+':
            print(f'Сумма чисел Х и Y равняется {x + y}')
        elif s == '-':
            print(f'Разность чисел Х и Y равняется {x - y}')
        elif s == '*':
            print(f'Произведение чисел Х и Y равняется {x * y}')
        elif s == '/':
            if y == 0:
                print('Деление на ноль не возможно!')
            else:
                print(f'Частное чисел Х и Y равняется {x / y}')
    else:
        print('Не верный знак операции.')
