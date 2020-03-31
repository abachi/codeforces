p = int(input())
rs = input().split(' ')
s = len(rs)
def easyOrHard():
    i=0
    while(i < s):
        if rs[i] == '1':
            print('HARD')
            return 0
        i+=1
    print('EASY')

easyOrHard()