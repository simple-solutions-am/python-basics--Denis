text = "Кто идет на мит? Я иду! Глеб, ты идешь на мит? Мит в субботу, не опаздывай, Глеб!"
text = text.lower()
punctuation = ".,!?;:-()'<>"
for char in punctuation:
    text = text.replace(char, "")

words = text.split()

counter = {}
for word in words:
    if word in counter:
        counter[word] += 1
    else:
        counter[word] = 1

repeated_words = {}
for word, count in counter.items():
    if count > 1:
        repeated_words[word] = count

most_word = ""
max_count = 0
for word, count in counter.items():
    if count > max_count:
        max_count = count
        most_word = word

print(repeated_words)
print(f"Самое частое: {most_word}")
