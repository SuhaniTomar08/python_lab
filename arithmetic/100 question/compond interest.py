# Read principal, rate, and time from standard input
p, r, t = map(float, input().split())

amount = p * (1 + r/100) ** t
ci = amount - p

print(ci)

#output
#1000 5 2
#102.5