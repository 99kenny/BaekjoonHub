n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
sum = 0
for i in range(n):
    minimum = min(a)
    a.remove(minimum)
    maximum = max(b)
    b.remove(maximum)
    sum += (maximum * minimum)

print(sum)
