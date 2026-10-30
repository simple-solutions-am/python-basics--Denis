commands = [
    ("add", "Макс", "+7 900 123-45-67"),
    ("add", "Глеб", "+7 911 765-43-21"),
    ("find", "Глеб"),
    ("find", "Илья"),
    ("del", "Макс"),
    ("del", "Денис"),
    ("add", "Саша", "+7 922 111-22-33"),
    ("list",)
]

book = {}

for cmd in commands:
    action = cmd[0]

    if action == "add":
        name = cmd[1]
        phone = cmd[2]
        book[name] = phone
        print(f"Сохранил:{name}")

    elif action == "find":
        name = cmd[1]
        if name in book:
            del book[name]
            print(f"Удалил {name}")
        else:
            print("Контак не найден.")

    elif action == "list":
        print(f"Контактов:{len(book)}")
        for name, phone in book.items():
            print(f"{name}: {phone}")
