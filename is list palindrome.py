# Function to check if a list is palindrome
def is_palindrome(lst):
    return lst == lst[::-1]  

input_list = input("Enter elements of the list separated by space: ").split()

input_list = [int(x) for x in input_list]

if is_palindrome(input_list):
    print("The list is a palindrome")
else:
    print("The list is not a palindrome")

    #output
    #Enter elements of the list separated by space: 1 2 3 2 1
    #The list is a palindrome