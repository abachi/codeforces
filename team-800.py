n=int(input())
ans=0
for i in range(0, n):
    if sum([int(x) for x in input().split(' ')])>1:
        ans+=1

print(ans)