sum_numbers = int(input("Введите сумму чисел: "))
product_numbers = int(input("Введите произведение чисел: "))

for x in range(1, 1001):
    for y in range(1, 1001):
        if x+y == sum_numbers and x*y == product_numbers:
            print("Задуманные числа Петей:", x, y)