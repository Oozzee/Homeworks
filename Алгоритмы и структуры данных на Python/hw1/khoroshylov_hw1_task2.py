n = 5
m = 6
print(f'{n} = {bin(n)}')
print(f'{m} = {bin(m)}')

print(f'{n} & {m} = {n & m} ({bin(n & m)})')
# n  m  &
# 1  1  1
# 0  1  0
# 1  0  0

print(f'{n} | {m} = {n | m} ({bin(n | m)})')
# n  m  |
# 1  1  1
# 0  1  1
# 1  0  1

print(f'{n} ^ {m} = {n ^ m} ({bin(n ^ m)})')
# n  m  ^
# 1  1  0
# 0  1  1
# 1  0  1

print(f'{n} << 2 = {n << 2} ({bin(n << 2)})')
# 101 << 2 = 10100 добавляем нули вконце

print(f'{n} >> 2 = {n >> 2} ({bin(n >> 2)})')
# 101 >> 2 = 1 убираем два символа
