# Recursive function to calculate power
def power(base, exponent):
    if exponent == 0:
        return 1  
    elif exponent < 0:
        return 1 / power(base, -exponent)  
    else:
        return base * power(base, exponent - 1) 
base = float(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))

result = power(base, exponent)

print(f"{base} raised to the power {exponent} is {result}")

#output
#Enter the base: 6
#Enter the exponent: 4
#6.0 raised to the power 4 is 1296.0