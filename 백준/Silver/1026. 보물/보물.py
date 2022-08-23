import sys

n = int(sys.stdin.readline())
a = [int(i) for i in sys.stdin.readline().split()]
b = [int(i) for i in sys.stdin.readline().split()]
sum = 0
for i in range(n):
    minimum = min(a)
    a.remove(minimum)
    maximum = max(b)
    b.remove(maximum)
    sum += (maximum * minimum)

print(sum)  
