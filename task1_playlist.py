
playlist = []
playlist.append("Утро")
playlist.append("Дорога")
playlist.append("Тренировка")
print(playlist)

# Шаг 2
print(len(playlist))
print(playlist[0], playlist[-1])
print(playlist[:2])
print("Дорога" in playlist)

# Шаг 3
playlist[1] = "Дорога домой"
playlist.insert(0, "Интро")
playlist.append("Финал")
skipped = playlist.pop()
playlist.remove("Утро")
print(f"{playlist} | пропустили: {skipped}")

# Шаг 4
for number, track in enumerate(playlist, start=1):
    print(f"{number}. {track}")
# for i in playlist: print(i + 1, i)
# Ошибка: i — это строка, а строка не поддерживает сложение с целым числом.

# Шаг 5
tracks = [("Интро", 95), ("Дорога домой", 214), ("Тренировка", 187), ("Финал", 241)]
first = tracks[0]
print(first, type(first))
title, seconds = first
print(title, seconds)
# first[1] = 100
# Ошибка: TypeError: 'tuple' object does not support item assignment
# Потому что кортежи неизменяемы.

# Шаг 6
total_seconds = 0
for _, seconds in tracks:
    total_seconds += seconds
minutes, remaining_seconds = divmod(total_seconds, 60)
print(f"Всего: {minutes:02}:{remaining_seconds:02}")

# Шаг 7
longest_name = tracks[0][0]
longest_duration = tracks[0][1]
short_tracks = []
for track_title, track_seconds in tracks:
    if track_seconds > longest_duration:
        longest_name = track_title
        longest_duration = track_seconds
    if track_seconds < 200:
        short_tracks.append(track_title)
print(f"Самый длинный: {longest_name}")
print(f"Короче 200 секунд: {short_tracks}")

# Шаг 8
names = ["Тренировка", "Интро", "Финал", "Дорога домой"]
print(sorted(names))
print(names)
result = names.sort()
print(result, names)
print(sorted(names, reverse=True)[:2])

# Шаг 9
queue = playlist
queue.append("Бонус")
print(playlist)
backup = playlist.copy()
backup.append("Еще один")
print(len(playlist), len(backup))
print(queue is playlist, backup is playlist)
# queue и playlist — это два имени для одного и того же списка.
# Поэтому append через queue меняет playlist.

# Шаг 10
lines = [f"🎧 Плейлист: {len(playlist)} трека, {minutes:02}:{remaining_seconds:02}"]
for number, (track_title, track_seconds) in enumerate(tracks, start=1):
    track_minutes, track_remaining_seconds = divmod(track_seconds, 60)
    lines.append(f"{number}. {track_title} - {track_minutes}:{track_remaining_seconds:02}")
print("\n".join(lines))

