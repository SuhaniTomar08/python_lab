# Function to sort a list in ascending order
def sort_list(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

input_list = input("Enter elements of the list separated by space: ").split()

input_list = [int(x) for x in input_list]

sorted_list = sort_list(input_list)

print("Sorted list:", sorted_list)

#output
#Enter elements of the list separated by space: 1
#Sorted list: [1]