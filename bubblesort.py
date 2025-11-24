import random
y = 10
items = [random.randint(0, 100) for x in range(y)]
n = len(items)-1
swapped = True
index = 0

while swapped and n > 0:
    swapped = False
    for index in range(0, n):
        if (items[index] > items[index+1]):
            temp = items[index]
            items[index] = items[index+1]
            items[index+1] = temp

            swapped = True

    n = n - 1

print(items)
