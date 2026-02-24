# Function to find the largest element in a list
def find_largest(lst):
    largest = lst[0]  # Initialize with first element
    for item in lst:
        if item > largest:
            largest = item
    return largest


input_list = input("Enter elements of the list separated by space: ").split()

input_list = [int(x) for x in input_list]

largest_element = find_largest(input_list)

print("The largest element in the list is:", largest_element)

#output
#Enter elements of the list separated by space:   1 2 3 5 8 9   
#The largest element in the list is: 9