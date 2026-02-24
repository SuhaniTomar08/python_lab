# Program to create student marks dictionary and find topper

students = {
    "Aman": 85,
    "Riya": 92,
    "Karan": 78,
    "Sneha": 88
}

topper = ""
highest = 0

for name in students:
    if students[name] > highest:
        highest = students[name]
        topper = name

print("Topper is", topper)
print("Marks =", highest)

#output
#Topper is Riya
#Marks = 92