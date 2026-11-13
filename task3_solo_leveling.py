xp = 1300
level = 1
need = 100
while xp >= need:
    level += 1
    need *= 2
    xp -= need // 2
print(f" Уровень: {level} \n Опыт: {xp} / {need}")
