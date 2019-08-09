import random
n = 20
mass = []
first_mass = []
second_mass = []
change_mass = []
for i in range(n):
    mass.append(random.randint(1, 99))
print(mass)
mass.sort()
print(mass)
num = int(input())
first_mass = mass[:num]
second_mass = mass[num:]
print(first_mass)
print(second_mass)
change_mass = second_mass + first_mass
print(change_mass)
