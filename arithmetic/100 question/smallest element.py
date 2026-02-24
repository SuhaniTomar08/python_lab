# Function to find the smallest element in a list
def find_smallest(lst):
    smallest = lst[0]  # Initialize with first element
    for item in lst:
        if item < smallest:
            smallest = item
    return smallest

input_list = input("Enter elements of the list separated by space: ").split()

input_list = [int(x) for x in input_list]

smallest_element = find_smallest(input_list)
1 
print("The smallest element in the list is:", smallest_element)

#output
#Enter elements of the list separated by space: 1 2 3 4 5 6 7
#The smallest element in the list is: 1