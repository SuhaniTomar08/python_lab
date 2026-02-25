<<<<<<< HEAD
# Program to find key with maximum value

data = {"A": 45, "B": 78, "C": 60}

max_key = ""
max_value = 0

for key in data:
    if data[key] > max_value:
        max_value = data[key]
        max_key = key

print("Key with maximum value:", max_key)
print("Value:", max_value)
"""Output:
Copy code

Key with maximum value: B
=======
# Program to find key with maximum value

data = {"A": 45, "B": 78, "C": 60}

max_key = ""
max_value = 0

for key in data:
    if data[key] > max_value:
        max_value = data[key]
        max_key = key

print("Key with maximum value:", max_key)
print("Value:", max_value)
"""Output:
Copy code

Key with maximum value: B
>>>>>>> 422e0177c51f10c37b5ebf1614fa14d3714e9bd1
Value: 78"""