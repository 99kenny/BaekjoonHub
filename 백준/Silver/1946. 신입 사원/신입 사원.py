import sys

t = int(sys.stdin.readline().rstrip())
for i in range(t):
    n = int(sys.stdin.readline().rstrip())
    score = [list(map(int,sys.stdin.readline().rstrip().split())) for i in range(n)]
    score.sort(key=lambda x : x[0])
    max = n + 1
    cnt = 0
    for j in score:
        if max > j[1] or j[0] == 1:
            max = j[1]
            cnt += 1
    print(cnt)