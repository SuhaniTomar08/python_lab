<<<<<<< HEAD
# Program to sort dictionary by values

data = {"a": 3, "b": 1, "c": 4, "d": 2}

items = list(data.items())

for i in range(len(items)):
    for j in range(i + 1, len(items)):
        if items[i][1] > items[j][1]:
            temp = items[i]
            items[i] = items[j]
            items[j] = temp

print("Sorted dictionary by values:")
for item in items:
    print(item[0], "->", item[1])
"""Output:
Copy code

Sorted dictionary by values:
b -> 1
d -> 2
a -> 3
=======
# Program to sort dictionary by values

data = {"a": 3, "b": 1, "c": 4, "d": 2}

items = list(data.items())

for i in range(len(items)):
    for j in range(i + 1, len(items)):
        if items[i][1] > items[j][1]:
            temp = items[i]
            items[i] = items[j]
            items[j] = temp

print("Sorted dictionary by values:")
for item in items:
    print(item[0], "->", item[1])
"""Output:
Copy code

Sorted dictionary by values:
b -> 1
d -> 2
a -> 3
>>>>>>> 422e0177c51f10c37b5ebf1614fa14d3714e9bd1
c -> 4"""