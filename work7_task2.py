def kd(kills, deaths):
    return kills / deaths if deaths > 0 else float(kills)

print(kd(3, 1))
print(kd(7, 2))
print(kd(5, 0))
