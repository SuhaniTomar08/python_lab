# Function to return unique elements from a list
def unique_elements(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst


input_list = input("Enter elements of the list separated by space: ").split()

input_list = [int(x) for x in input_list]

result = unique_elements(input_list)

print("Unique elements:", result)

#output
#Enter elements of the list separated by space: 1 2 3 4 5 6 
#Unique elements: [1, 2, 3, 4, 5, 6]