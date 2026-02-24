# Read integer from standard input
num = int(input())

# Handle negative numbers
if num < 0:
    print("Not an Armstrong Number")
else:
    temp = num
    n = len(str(num))  # Number of digits
    sum_digits = 0

    # Calculate sum of digits raised to the power n
    while temp > 0:
        digit = temp % 10
        sum_digits += digit ** n
        temp = temp // 10

    # Check Armstrong condition
    if sum_digits == num:
        print("Armstrong Number")
    else:
        print("Not an Armstrong Number")

        #output
        #153
        #Armstrong Number