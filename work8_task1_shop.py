
def show_menu(shop):
    print("Магазин:")
    for item, price in shop.items():
        print(item, "-", price)


def check(item, gold):
    if item not in shop:
        return "Нет в магазине"

    price = shop[item]
    if item in ("меч", "щит") and item in bag:
        return f"{item.capitalize()} уже есть в сумке"
    if gold < price:
        return f"Не хватает {price - gold} золота"

    return ""
    

shop = {"меч": 300, "щит": 200, "зелье": 50}
gold = 500
bag = []

if __name__ == "__main__":
    show_menu(shop)

    while True:
        item = input("Что купить? ").strip()

        if item == "/stop":
            print("В сумке:", bag, "Золото:", gold)
            break

        error = check(item, gold)
        if error:
            print(error)
            continue

        gold -= shop[item]
        bag.append(item)
        print(f"Куплено: {item}, золото осталось: {gold}")
