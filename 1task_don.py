donations = [
    ("max", 100),
    ("lena", 0),
    ("kir", 500),
    ("max", 250),
    ("anon", 50),
]

paid_donations = [(name, amount) for name, amount in donations if amount > 0]
total = sum(amount for _, amount in paid_donations)
donation_count = len(paid_donations)
top_name, top_amount = max(paid_donations, key=lambda donation: donation[1])
average = total / donation_count

print(f"Сумма: {total}")
print(f"Донатов: {donation_count}")
print(f"Топ: {top_name} {top_amount}")
print(f"средний донат без нулевых: {average:g}")