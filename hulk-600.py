n = int(input())
i=0
feelings = ''
while i < n:
    if i+1 == n:
        prefix = 'it'
    else:
        prefix = 'that'
    
    if i % 2 == 0:
        feelings += ' I hate ' + prefix
    else:
        feelings += ' I love ' + prefix
    i+= 1

print(feelings.strip())
