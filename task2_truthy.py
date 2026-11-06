#1 False True True True False
# Правильно: False False False False False — пустые кортеж, словарь и множество тоже ложны.
print(bool(0.0), bool(()), bool({}), bool(set()), bool(None))
#2 False
# Правильно: True True True True — непустые строки и список истинны, как и ненулевое число.
print(bool("None"), bool(-1), bool(" "), bool([[]]))
#3 False True True False
# Правильно: True True False False — not возвращает отрицание истинности значения.
print(not 0, not "", not "0", not [0])
#4 False False True True
print(None == 0, None == "", None == None, None is None)
#5 [1,2,3] [1,2,3]
# Правильно: [1, 2, 3] None — append изменяет список, но сам возвращает None.
x = [1, 2]
y = x.append(3)
print(x, y)
#6 0 False False
# Правильно: 0 None нет — get без значения по умолчанию возвращает None для отсутствующего ключа.
d = {"a": 0}
print(d.get("a"), d.get("b"), d.get("b", "нет"))
#7 пусто 5 нет да
print("" or "пусто", 0 or 5, None or "нет", "да" or "нет")
#8 False
# Правильно: TypeError — сравнение None и числа оператором > в Python 3 не поддерживается.
score = None
print(score > 5)
#9 Еще не играл
score = 0
if score:
    print("Результат:", score)
else:
    print("Еще не играл")
#10 Есть текст
score = 10
score = 0
score = None

text = "   "
if text:
    print("Есть текст")
else:
    print("Пусто")