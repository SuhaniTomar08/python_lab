# Function to remove duplicates from a list
def remove_duplicates(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst

input_list = input("Enter elements of the list separated by space: ").split()

input_list = [int(x) for x in input_list]

result = remove_duplicates(input_list)

print("List after removing duplicates:", result)

#output
#Enter elements of the list separated by space: 7
#List after removing duplicates: [7]