import random


def hit(dmg):
    if random.randint(1, 4) == 1:
        return f"Критический удар! Нанесено {dmg * 2} урона"
    return f"Обычный удар! Нанесено {dmg} урона"

for i in range(10):
    print(hit(10))
    