# Read the number of terms from the user
n = int(input("Enter the number of terms: "))

a, b = 0, 1
count = 0

while count < n:
    print(a, end=" ")
    a, b = b, a + b  # Update values
    count += 1

    #output
    #Enter the number of terms:5
    #0 1 1 2 3