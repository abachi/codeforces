
# a*3 each 1 year 
# b*2 each 1 year
args = input().split(' ')
a = int(args[0])
b = int(args[1])
years = 0
while a <= b:
    a *= 3
    b *= 2
    years +=1

print(years)
