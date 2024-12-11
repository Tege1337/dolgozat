# A CSOPORT

"""
Szimuláljuk egy 20 oldalú D&D kocka 100 db dobását! A dobásokat egy listában tároljuk! Majd oldjuk meg a következő feladatokat!
Minden feladat előtt a program írja ki a feladat sorszámát!

1. Volt-e 6-os a dobások között?
2. Hányadikra sikerült először 18-nál nagyobbat dobni?
3. Hány darab 1-est dobtak?
4. Melyik volt a legnagyobb dobás a 10-nél kisebbek közül, és hányadik dobás volt?
5. Mennyi a 4-es dobások szorzata?
"""

import random

# generating

rolls = []
for x in range(100):
    rolls.append(random.randint(1, 20))
print(rolls)

# task no 1
# Volt-e 6-os a dobások között?

hatos = False
hatos_times = 0
for number in rolls:
    if number == 6:
        hatos = True
        hatos_times += 1

print("\n-----------------------------------------------------------")
print(f"{hatos}, hogy volt 6-os a dobott számok között. ")
print(f"{hatos_times} alkalommal dobtál 6-ost. ")
print("-----------------------------------------------------------\n")

# task no 2
# Hányadikra sikerült először 18-nál nagyobbat dobni?

greater_than_18 = next(x for x, number in enumerate(rolls) if number > 18)

print("-----------------------------------------------------------")
print(f"A {greater_than_18 + 1}. dobásod lett az első nagyobb mint 18. ")
print("-----------------------------------------------------------\n")

# task no 3
# Hány darab 1-est dobtál

egyes = 0
for number in rolls:
    if number == 1:
        egyes += 1

print("-----------------------------------------------------------")
print(f"{egyes} alkalommal dobtál 1-est. ")
print("-----------------------------------------------------------\n")

# task no 4
# Melyik volt a legnagyobb dobás a 10-nél kisebbek közül, és hányadik dobás volt?

less_10 = []
for number in rolls:
    if number < 10:
        less_10.append(number)
biggest_less_10 = rolls.index(max(less_10))

print("-----------------------------------------------------------")
print(f"{biggest_less_10}. dobásod volt a legnagyobb 10 alatti szám. ")
print("-----------------------------------------------------------\n")

# task no 5
# Mennyi a 4-es dobások szorzata?

exponential = 1
for x in rolls:
    if x == 4:
        exponential += 1

print("-----------------------------------------------------------")
print(f"{4 ** exponential} a négyesek szorzata ebben a listában. ")
print("-----------------------------------------------------------\n")