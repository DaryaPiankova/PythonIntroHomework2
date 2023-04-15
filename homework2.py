n = int(input('Введите кол-во монет: '))
countReshka = 0
countGerb = 0
for i in range(n):
    coin = int(input('Введите сторону монеты: '))
    if coin == 0:
        countReshka += 1
    else:
        countGerb += 1
if countGerb > countReshka:
    print(countReshka)
else:
    print(countGerb)
