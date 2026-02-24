# Read weight (kg) and height (m) from standard input
weight, height = map(float, input().split())

bmi = weight / (height ** 2)

if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 24.9:
    category = "Normal weight"
elif 25 <= bmi < 29.9:
    category = "Overweight"
else:
    category = "Obese"

print(category)

#output
#70 1.75
#Normal weight