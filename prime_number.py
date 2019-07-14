n = input('Введите порядковый номер числа: ')
mass = []
for i in range(2, 100):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        mass.append(i)
print(mass[int(n) - 1])
