# Function to calculate sum of list elements
def sum_of_list(lst):
    total = 0
    for num in lst:
        total += num
    return total


input_list = input("Enter elements of the list separated by space: ").split()

input_list = [int(x) for x in input_list]

total_sum = sum_of_list(input_list)

print("Sum of list elements is:", total_sum)

#output
#Enter elements of the list separated by space: 1 2 3 4 5
#Sum of list elements is: 15