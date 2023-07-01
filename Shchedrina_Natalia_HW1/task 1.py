num = int(input("Введите трехзначное число: "))
d1 = num // 100
d2 = num % 100 // 10
d3 = num % 10
sum = d1 + d2 + d3
print(sum)