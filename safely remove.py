<<<<<<< HEAD
# Program to safely remove a key from dictionary

data = {"a": 1, "b": 2, "c": 3}

key = input("Enter key to remove: ")

if key in data:
    del data[key]
    print("Key removed")
else:
    print("Key not found")

print("Updated dictionary:", data)
"""Output:
Copy code

Enter key to remove: b
Key removed
=======
# Program to safely remove a key from dictionary

data = {"a": 1, "b": 2, "c": 3}

key = input("Enter key to remove: ")

if key in data:
    del data[key]
    print("Key removed")
else:
    print("Key not found")

print("Updated dictionary:", data)
"""Output:
Copy code

Enter key to remove: b
Key removed
>>>>>>> 422e0177c51f10c37b5ebf1614fa14d3714e9bd1
Updated dictionary: {'a': 1, 'c': 3}"""