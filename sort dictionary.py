# Program to sort dictionary by keys

data = {"b": 2, "a": 1, "d": 4, "c": 3}

keys = list(data.keys())

for i in range(len(keys)):
    for j in range(i + 1, len(keys)):
        if keys[i] > keys[j]:
            temp = keys[i]
            keys[i] = keys[j]
            keys[j] = temp

print("Sorted dictionary by keys:")
for key in keys:
    print(key, "->", data[key])
"""Output:
Copy code

Sorted dictionary by keys:
a -> 1
b -> 2
c -> 3
d -> 4"""