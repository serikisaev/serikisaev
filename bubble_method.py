from random import randint

n = 5
mass = []
for i in range(n):
    mass.append(randint(1, 99))
print(mass)
print("--------------------------------------")

for i in range(n-1):
    for j in range(n-i-1):
        if mass[j] > mass[j+1]:
            mass[j], mass[j+1] = mass[j+1], mass[j]
    print(mass)
