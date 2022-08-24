import sys

eq = sys.stdin.readline()
tok = eq.split("-")
result = 0
for i in range(0,len(tok)):
    t = tok[i]
    a = 0
    if str.isdigit(t):
        a = int(t)
    else:
        values = t.split("+")
        for j in values:
            a += int(j)

    if i== 0:
        result += a
    else:
        result -= a 
            
print(result)