import random

def q_sort(mass):
    if len(mass) <= 1:
       return mass
    else:
        first_mass = []
        second_mass = []
        third_mass = []
        a = random.choice(mass)
        for i in mass:
            if i < a:
                first_mass.append(i)
            elif i > a:
                second_mass.append(i)
            else:
                third_mass.append(i)
        return q_sort(first_mass) + third_mass + q_sort(second_mass)
    
n = 15
pikabu = []
for i in range(n):
    pikabu.append(random.randint(1, 99))
print(pikabu)
print("--------------------------------------")
print(q_sort(pikabu))
