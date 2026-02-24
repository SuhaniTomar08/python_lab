# Read marks from standard input
marks = float(input())

# Assign grades
if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
else:
    grade = "F"

# Print the grade
print(grade)

#output
#85
#B