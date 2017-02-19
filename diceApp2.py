from random import randint

sides = int(input("How man sides?: "))
dSides = sides

dSides = randint(1, dSides)

dNumber = int(input("How many dice do you need to roll?: "))

roll = dSides * dNumber

print(roll)
