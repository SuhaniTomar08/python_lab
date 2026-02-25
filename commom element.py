# Function to find common elements
def common_elements(list1, list2):
    common = []
    for item in list1:
        if item in list2 and item not in common:
            common.append(item)
    return common

list1 = input("Enter elements of the first list separated by space: ").split()
list1 = [int(x) for x in list1]  
list2 = input("Enter elements of the second list separated by space: ").split()
list2 = [int(x) for x in list2]  
result = common_elements(list1, list2)

print("Common elements between the two lists:", result)


#output
#Enter elements of the first list separated by space: 1 2 3 4
#Enter elements of the second list separated by space: 3 4 5 6
#Common elements between the two lists: [3, 4]