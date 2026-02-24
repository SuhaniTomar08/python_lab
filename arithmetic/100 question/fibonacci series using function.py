# Function to generate Fibonacci series of n terms
def fibonacci_series(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

n_terms = int(input("Enter the number of terms: "))

fib_series = fibonacci_series(n_terms)
print("Fibonacci series:", fib_series)

#output
#Enter the number of terms: 23
#Fibonacci series: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711]