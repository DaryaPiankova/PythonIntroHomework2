summa = int(input('Введите первое число: '))
multipl = int(input('Введите второе число: '))
num1 = 0
num2 = 0
for i in range(multipl):
    for i in range(summa):
        if num1*num2 == multipl and num1+num2 == summa:
            print(num1, num2)
            break
        else:
            num2 += 1
    num1 += 1
    num2 = 0
