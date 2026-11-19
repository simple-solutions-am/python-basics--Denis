events = [
    "kill", "kill", "afk",
    "death", "kill", "afk",
    "end", "kill"
]

kill_count = 0
death_count = 0

for event in events:
    if event == "end":
        break
    if event == "kill":
        kill_count += 1
    if event == "death":
        death_count += 1
k_d = kill_count / death_count if death_count > 0 else float('inf')
print(f"Kills: {kill_count}")
print(f"Deaths: {death_count}")
print(f"K/D: {k_d}")
