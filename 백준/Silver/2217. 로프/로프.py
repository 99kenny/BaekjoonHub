import sys

n = int(sys.stdin.readline())
ropes = [int(sys.stdin.readline().rstrip()) for i in range(n)]
ropes.sort()
result = 0
for i in range(n):
    minimum = min(ropes)
    if result < minimum * (n - i):
        result = minimum * (n - i)
    ropes.remove(minimum)

print(result)