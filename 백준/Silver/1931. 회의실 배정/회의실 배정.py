n = int(input())
time = []
cnt = 1
for i in range(n):
    time.append(list(map(int,input().split())))

time.sort(key = lambda x : x[0])
time.sort(key = lambda x : x[1])

temp = time[0][1]
for i in range(1,n):
    if time[i][0] >= temp:
        cnt += 1
        temp = time[i][1]

print(cnt)