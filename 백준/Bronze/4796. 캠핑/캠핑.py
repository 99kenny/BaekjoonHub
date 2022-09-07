import sys

l = []
cond = 0
while cond == 0: 
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    if a[0] == 0 and a[1] == 0 and a[2] == 0:
        break
    l.append(a)

for i in range(len(l)):
    n = l[i][2] // l[i][1]
    r = l[i][2] % l[i][1]
    if r > l[i][0]:
        r = l[i][0]
    print("Case " + str(i+1) + ": " + str(n*l[i][0] + r)) 