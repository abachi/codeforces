n = int(input())
words=[]
for i in range(0, n):
    words.append(input())

for w in words:
    size = len(w)
    if size > 10:
        print(w[0]+str(size-2)+w[size-1])
    else:
        print(w)