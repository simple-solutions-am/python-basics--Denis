import random


def loot():
    global gold
    if random.choice(["золото", "зелье", "пусто"]) == "золото":
        gold += 100
        

gold = 500

if __name__ == "__main__":
    for i in range(5):
        loot()
    print(f"У вас {gold} золота")