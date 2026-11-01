s = "Python - лучший язык. Учу Python каждый день!"

print("Python" in s, "python" in s)

index_1 = s.find("Python")
index_2 = s.find("Python", index_1 + 1)
print(index_1, index_2)

find_java = s.find("Java")
print(find_java)

python_count = s.count("Python")
print(python_count)

print(s.replace("Python", "Питон"))

print(s.replace("Python", "Питон", 1))

a = "Клуб"
b = "клуб"
print(a == b, a.lower() == b.lower(), "кит" < "кот")

phrase = "А роза упала на лапу Азора"
phrase_new = phrase.lower().replace(" ", "")
print(phrase_new)

print(phrase_new == phrase_new[::-1])

hi = "Привет мир"
hi_new = hi.lower().replace(" ", "")
print(hi_new == hi_new[::-1])
