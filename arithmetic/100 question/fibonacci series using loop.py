# Read the number of terms
n = int(input("Enter the number of terms: "))

a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

    #output
    #Enter the number of terms: 8
    #0 1 1 2 3 5 8 13 