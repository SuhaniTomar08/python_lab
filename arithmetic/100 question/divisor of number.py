# Read input number
num = int(input("Enter a number: "))

print("Divisors of", num, "are:")

for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=" ")

        #output
        #Enter a number: 14
        #Divisors of 14 are:
        #1 2 7 14