# Function to reverse a list
def reverse_list(lst):
    reversed_lst = []
    for i in range(len(lst)-1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst

input_list = input("Enter elements of the list separated by space: ").split()

input_list = [int(x) for x in input_list]

reversed_list = reverse_list(input_list)

print("Reversed list:", reversed_list)

#output
#Enter elements of the list separated by space: 8
#Reversed list: [8]