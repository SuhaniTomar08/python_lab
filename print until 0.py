# Initialize sum
total = 0

while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    total += num

print("Sum:", total)

#output
#Enter a number (0 to stop): 5
#Enter a number (0 to stop): 3
#Enter a number (0 to stop): 6
#Enter a number (0 to stop): 0
#Sum: 14