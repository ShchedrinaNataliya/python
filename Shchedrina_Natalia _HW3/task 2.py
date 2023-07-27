N = int(input("Введите количество элементов в массиве: "))
A = []
for i in range(N):
    A.append(int(input("Введите элемент массива: ")))

X = int(input("Введите число X: "))

closest_element = A[0]
closest_diff = abs(X - A[0])

for i in range(1, N):
    diff = abs(X - A[i])
    if diff < closest_diff:
        closest_element = A[i]
        closest_diff = diff

print("Самый близкий элемент к числу", X, "в массиве", A, "это", closest_element)