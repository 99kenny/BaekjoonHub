import sys

time = int(sys.stdin.readline())
a = 0
b = 0
c = 0

if time // 300 > 0:
    a = time // 300
    time = time % 300

if time // 60 > 0:
    b = time // 60
    time = time % 60

if time // 10 > 0:
    c = time // 10
    time = time % 10

if time == 0:
    print(str(a) + " " + str(b) + " " + str(c))
else:
    print(-1)