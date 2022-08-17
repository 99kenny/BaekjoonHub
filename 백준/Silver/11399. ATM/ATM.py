num = int(input())
time = list(map(int, input().split(" ")))
result = []
sumTime = 0
for i in range(0,num):
    minimum = min(time)
    result.append(minimum)
    time.remove(minimum)
    sumTime += sum(result)

print(sumTime)
