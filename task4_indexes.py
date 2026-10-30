nums = [10, 20, 30, 40, 50]
m = [[1, 2], [3, 4], [5, 6]]
s = "бот-бот"


print(nums[2:100], nums[10:])

print(nums[::-2], nums[3:0:-1], nums[0:3:-1])

print(m[1][0], m[-1][-1], len(m))

print(m[1:][0], m[1][:1])

print(s.find("T"), s.find("я"), nums.index(40))

print("\n Бот чистит спам ")

msgs = ["спам", "привет", "спам", "спам", "пока"]

for x in msgs.copy(): 
    if x == "spam" or x == "спам":
        msgs.remove(x)

print(msgs) 


print("\n Рост онлайна ")
online = [3, 5, 4, 8]
diff = []

for i in range(len(online) - 1):
    diff.append(online[i + 1] - online[i])


print(diff)

