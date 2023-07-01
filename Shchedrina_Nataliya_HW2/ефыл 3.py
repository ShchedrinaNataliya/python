numbers_coins = int(input("Введите количество монеток: "))
coins = input("Введите состояние монеток (H - решка, T - герб): ")

res_heads = coins.count("H")
res_tails = coins.count("T")

min_flips = min(res_heads, res_tails)
print("Минимальное количество монет, которые нужно перевернуть:", min_flips)