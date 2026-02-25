# Function to calculate average of list elements
def average_of_list(lst):
    if len(lst) == 0:
        return 0 
    total = 0
    for num in lst:
        total += num
    return total / len(lst)

input_list = input("Enter elements of the list separated by space: ").split()

input_list = [int(x) for x in input_list]

avg = average_of_list(input_list)

print("Average of list elements is:", avg)

#output
#Enter elements of the list separated by space: 2 4 6 8
#Average of list elements is: 5.0