n = input('Введите число для вычисление факториала: ')
fact = 1
for i in range(1, int(n) + 1):
    fact = i * fact
print(fact)
