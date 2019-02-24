for i in range(32, 129):
    print(f'{i}{chr(i)}|', end='')
    if i % 10 == 1:
        print()
