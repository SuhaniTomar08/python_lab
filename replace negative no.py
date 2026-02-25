# Function to replace negative numbers with zero
def replace_negatives(lst):
    for i in range(len(lst)):
        if lst[i] < 0:
            lst[i] = 0
    return lst

input_list = input("Enter elements of the list separated by space: ").split()

input_list = [int(x) for x in input_list]

result_list = replace_negatives(input_list)

print("List after replacing negative numbers with zero:", result_list)


#output
#Enter elements of the list separated by space: 4 -3 7 -1 0
#List after replacing negative numbers with zero: [4, 0, 7, 0, 0]