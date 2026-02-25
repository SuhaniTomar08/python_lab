# Read four numbers from standard input
a, b, c, d = map(float, input().split())

greatest = a

if b > greatest:
    greatest = b
if c > greatest:
    greatest = c
if d > greatest:
    greatest = d

print(greatest)

#output
#12 45 7 33
#45