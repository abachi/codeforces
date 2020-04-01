m = []
for i in range(0, 5):
    m.append([ int(x) for x in input().strip().split(' ')])
ans = 0
for i in range(0, 5):
    for j in range(0, 5):
        if m[i][j] == 1:
            ans = abs(i-2) + abs(j-2)
            break
print(ans)