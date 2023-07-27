num_in_general = int(input("Введите количество элементов в массиве: "))
A = []
for i in range(num_in_general):
    num = int(input("Введите число: "))
    A.append(num)

num_x = int(input("Введите число X: "))

count = 0
for num in A:
    if num == num_x:
        count += 1

print("Число", num_x, "встречается", count, "раз(а) в массиве.")