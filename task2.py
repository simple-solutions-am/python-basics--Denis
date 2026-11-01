digits = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(digits[-1:-3:-1])
print(digits[5], digits[-4])
print(digits[2:6:1])
print(digits[::2])
print(digits[::-1])
print(digits.count(1), digits.count(5))
print(max(digits), min(digits), sum(digits))
print(digits.index(5))
print(len(digits)- 1 - digits[::-1].index(5))
indeces = []
for index, value in enumerate(digits):
    if value == 5:
        indeces.append(index)
print(indeces)
if 7 in digits:
    print(digits.index(7))
else:
    print("7 не найдено")
new_list = [0 if x == 5 else x for x in digits]
print(new_list)
print(digits)