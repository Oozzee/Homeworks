symbol = int(input('Задайте номер буквы в алфавите от 1 до 26: '))
symbol = symbol + ord('a') - 1
print(f'Это буква {(chr(symbol))}')
