a = ord(input('Введите первую букву: '))
b = ord(input('Введите вторую букву: '))
a = a - ord('a') + 1
b = b - ord('a') + 1
print(f'Позиции букв в алфавите: {a} и {b}')
print(f'Между буквами расположено символов: {abs(b - a - 1)}.')
