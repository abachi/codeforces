x = int(input())
s= 0
moves = 0
while True:
    if moves + 5 <= x:
        moves+=5
        s+=1
        continue
    elif moves + 4 <= x:
        moves+= 4
        s+=1
        continue
    elif moves + 3 <= x:
        moves+= 3
        s+=1
        continue
    elif moves + 2 <= x:
        moves+= 2
        s+=1
        continue
    elif moves + 1 <= x:
        moves+= 1
        s+=1
        continue

    if moves == x:
        break

print(s)