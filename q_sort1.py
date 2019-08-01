import random

def q_sort(mass):
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
    
pikabu = [5,9,7,6,2,4,56,6,8,5]
print(pikabu)
print("--------------------------------------")
q_sort(pikabu)
