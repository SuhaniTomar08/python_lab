# Function to separate even and odd numbers
def separate_even_odd(lst):
    even = []
    odd = []
    for num in lst:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return even, odd

input_list = input("Enter elements of the list separated by space: ").split()

input_list = [int(x) for x in input_list]

even_numbers, odd_numbers = separate_even_odd(input_list)

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)

#output
#Enter elements of the list separated by space: 1 2 3 4 5 6
#Even numbers: [2, 4, 6]
#Odd numbers: [1, 3, 5]