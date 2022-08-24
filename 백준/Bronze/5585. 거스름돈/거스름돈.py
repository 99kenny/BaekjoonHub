import sys

m = 1000 - int(sys.stdin.readline())
cnt = 0
cnt += (m//500)
m = m % 500
cnt += (m//100)
m = m % 100
cnt += (m//50)
m = m % 50
cnt += (m//10)
m = m % 10
cnt += (m//5)
m = m % 5
cnt += m

print(cnt)