anya = {"игры", "футбол", "боты", "аниме"}
lev = {"аниме", "музыка", "игры", "шахматы"}
kira = {"футбол", "код", "боты"}

print(sorted(anya & lev))
print(sorted(anya | lev | kira))
print(sorted(lev - anya - kira))
print(not lev.isdisjoint(kira), not anya.isdisjoint(kira))
tags = ["python", "бот", "игры", "python", "aiogram", "бот", "python"]
print(len(tags), len(set(tags)))
print(sorted(set(tags)))