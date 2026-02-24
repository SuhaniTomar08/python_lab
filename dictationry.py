# Program to merge two dictionaries manually

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged = {}

for key in dict1:
    merged[key] = dict1[key]

for key in dict2:
    merged[key] = dict2[key]

print("Merged dictionary:", merged)
#Output:
#Copy code

#Merged dictionary: {'a': 1, 'b': 2, 'c': 3, 'd': 4}