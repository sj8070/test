n = int(input())

a = [[0] * n for i in range(n)]
a[0][1] = 1

for i in a:
    print(' '.join([str(elem) for elem in i]))

print(' ')
    
for i in range(n):
    print(' '.join(str(a[j][i]) for j in range(n)))