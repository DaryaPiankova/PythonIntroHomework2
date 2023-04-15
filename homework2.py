summa = int(input('Введите первое число: '))
multipl = int(input('Введите второе число: '))
num1 = 0
num2 = 0
for num1 in range(multipl):
    for num2 in range(summa):
        if num1*num2 == multipl and num1+num2 == summa:
            print(num1, num2)
           
      
