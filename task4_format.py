numbers = [7, 74, 743, 7438]
print("".join(f"{num:03d}" for num in numbers))

ex2 = f"{1499.5:.2f}"
print(ex2)

ex3 = f"{1234567.891:,.2f}"
print(ex3)

ex4 = f"{1234567.891:,.2f}".replace(",", " ")
print(ex4)

ex5 = 0.875 * 100
print(ex5)

day = 5
month = 3
year = 2027
print(f"{day:02d}.{month:02d}.{year}")

print(f"{"Чек":*^20}")

cart = [("Хлеб", 45), ("Молоко", 89), ("Чокопай", 120)]
for name, price in cart:
    print(f"{name:<10}{price:>6} руб.")

total_price = sum(price for _,price in cart)
print(f"Итого: {total_price} руб.")
