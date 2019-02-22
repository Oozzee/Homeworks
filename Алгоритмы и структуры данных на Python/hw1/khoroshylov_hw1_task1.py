num = int(input("Введите трехзначное число: "))

num1 = num // 100
num2 = num % 100 // 10
num3 = num % 10

print("Сумма цифр числа:", num1 + num2 + num3)
print("Произведение цифр числа:", num1 * num2 * num3)
