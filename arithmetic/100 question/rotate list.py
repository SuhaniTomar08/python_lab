# Function to rotate list by k positions
def rotate_list(lst, k):
    n = len(lst)
    k = k % n 
    return lst[-k:] + lst[:-k] 

input_list = input("Enter elements of the list separated by space: ").split()
input_list = [int(x) for x in input_list] 

k = int(input("Enter number of positions to rotate: "))

rotated_list = rotate_list(input_list, k)

print(f"List after rotating by {k} positions:", rotated_list)

#output
#Enter elements of the list separated by space: 2 3 4 5 2 4 
#Enter number of positions to rotate: 2
#List after rotating by 2 positions: [2, 4, 2, 3, 4, 5]