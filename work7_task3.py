def solo_leveling(xp, level, need):
    while xp >= need:
        level += 1
        need *= 2
        xp -= need//2
    return f" Уровень: {level} \n Опыт: {xp} / {need}"

print(solo_leveling(1300, 1, 100))
