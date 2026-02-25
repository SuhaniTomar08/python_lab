# Function to find the maximum of three numbers
def maximum(a, b, c):
    return max(a, b, c)  

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

max_num = maximum(num1, num2, num3)
print(f"The maximum of {num1}, {num2}, and {num3} is {max_num}")

#output
#Enter first number: 23
#Enter second number: 32
#Enter third number: 4
#The maximum of 23.0, 32.0, and 4.0 is 32.0