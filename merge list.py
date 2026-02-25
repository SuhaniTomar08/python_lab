# Function to merge two lists and remove duplicates
def merge_and_unique(list1, list2):
    merged = list1 + list2
    unique_list = []
    for item in merged:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


list1 = input("Enter elements of the first list separated by space: ").split()
list1 = [int(x) for x in list1]  

list2 = input("Enter elements of the second list separated by space: ").split()
list2 = [int(x) for x in list2]  
result = merge_and_unique(list1, list2)

print("Merged list without duplicates:", result)

#output
#Enter elements of the first list separated by space: 1 2 3 4
#Enter elements of the second list separated by space: 3 4 5 6
#Merged list without duplicates: [1, 2, 3, 4, 5, 6]