banned = {"спам", "реклама"}
msg = "купи спам и реклама тут"

words = msg.split()
replaced_count = sum(word in banned for word in words)
msg = " ".join("***" if word in banned else word for word in words)

print(msg)
print(f"Заменено слов: {replaced_count}")
    