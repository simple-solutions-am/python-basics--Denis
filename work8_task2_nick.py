taken = {"shadow", "shadow1", "shadow2", "shadow4"}

def free_nick(nick, taken):
    candidate = nick
    number = 1
    while candidate in taken:
        candidate = f"{nick}{number}"
        number += 1
    taken.add(candidate)
    return candidate


print(free_nick("shadow", taken))
print(free_nick("neo", taken))