# Read the upper limit
N = int(input("Enter N: "))

num = 2

while num <= N:
    
    is_prime = True
    divisor = 2
    while divisor <= num // 2:
        if num % divisor == 0:
            is_prime = False
            break
        divisor += 1
    if is_prime:
        print(num, end=" ")
    num += 1

    #output
    #Enter N: 8
    #2 3 5 7 