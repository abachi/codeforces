n = int(input())
results = []
for i in range(0, n):
    s =sum([int(x)  for x in input().split(' ')])
    results.append(s//2)

for i in results:
    print(i)