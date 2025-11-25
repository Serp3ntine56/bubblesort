import random
y = 10
items = [random.randint(0, 100) for x in range(y)]
n = len(items)-1
index = 0

for x in range(0, n):
    for index in range(0, n):
        if (items[index] > items[index+1]):
            temp = items[index]
            items[index] = items[index+1]
            items[index+1] = temp
            
print(items)
