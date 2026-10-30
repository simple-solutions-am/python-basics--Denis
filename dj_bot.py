requests = [
    ("max", "Интро"),
    ("lena", "Финал"),
    ("max", "Дорога домой"),
    ("kira", "Интро"),
    ("lena", "Интро"),
    ("tim", "Тренировка"),
    ("max", "Интро"),
    ("kira", "Финал")
]
print(f"Заявок: {len(requests)}")

users = set()
for user, track in requests:
    users.add(user)

print(f"Кто писал: {user}")

count = {}
for user, track in requests:
    count[track] = count.get(track, 0) + 1

print(f"Треки: {count}")

print(count["Финал"])
print(count.get("Космос", 0))

print("\n5 Перебор словаря:")
for trak, n in count.items():
    print(f"{track}: {'🔥' * n}")

best_track = None
max_requests = -1

for track, num in count.items():
    if num > max_requests:
        max_requests = num
        best_track = track

print(f"\n Хит вечера:\nХит вечера: {best_track} ({max_requests})")   

by_user = {}
for user, track in requests:
    if user not in by_user:
        by_user[user] = set()
    by_user[user].add(track)

print(f"\n Треки max по алфавиту:\n{sorted(by_user['max'])}")

lena = by_user["lena"]
kira = by_user["kira"]
max = by_user["max"]
print("\n8 Похожие вкусы:")
print(f"1) {sorted(lena & max)}")
print(f"2) {sorted(max - lena)}")
print(f"3) {sorted(lena | max)}")
print(f"4) {lena == kira}")
