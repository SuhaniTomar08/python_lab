# Read base and exponent from user
base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))

result = 1

for i in range(exponent):
    result *= base

print(f"{base} raised to the power {exponent} is: {result}")

#output
#Enter the base: 8
#Enter the exponent: 3
#8 raised to the power 3 is: 512