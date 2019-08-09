import random
n = 20
mass = []
for i in range(n):
    mass.append(random.randint(1, 99))
print(mass)
mass.sort()
print(mass)
isk = int(input())

l = 0
h = n - 1
while l <= h:
    m = (l + h) // 2
    if isk < mass[m]:
        h = m - 1
    elif isk > mass[m]:
        l = m + 1
    else:
        print(m)
        break
else:
    print("Не найдено")
