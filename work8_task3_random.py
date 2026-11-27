import random

count = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

def roll(sides):
    return random.randint(1, sides)

for i in range(600):
    result = roll(6)
    count[result] += 1

print(f"один {count[1]}, два {count[2]}, три {count[3]}, четыре {count[4]}, пять {count[5]}, шесть {count[6]}")