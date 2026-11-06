people = 47
seats = 12

bus = (people // seats)
if people % seats:
    bus += 1
free_seats =(bus * seats) - people
print(f"Количество автобусов: {bus}, свободных мест {free_seats} ")

msg = " /remind 90 купить хлеб "

parts = msg.strip().split()
if not(parts and parts[0].startswith("/remind")):
    print('Не команда')
elif len(parts) < 3 or not parts[1].isdigit():
    print("Время - числом")
else:
    minutes = int(parts[1])
    text = ''.join(parts[2:])
    h, m = divmod(minutes, 60)
    if h:
        print(f"Напомни через {h} часов {m} минут : {text}")
    else:
        print(f"Напомни через {m} минут : {text}")