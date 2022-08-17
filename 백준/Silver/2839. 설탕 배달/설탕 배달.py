weight = int(input())
sum = weight
cnt = 0
while sum >= 5:
    sum -= 5
    cnt += 1
fcnt = cnt

while True:
    while sum >= 3:
        sum -= 3
        cnt += 1
    if sum == 0:
        print(cnt)
        break
    else:
        if fcnt == 0:
            print(-1)
            break
        else:
            fcnt -= 1
            cnt -= 1
            sum += 5