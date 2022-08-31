from posixpath import split
import sys

n = int(sys.stdin.readline())
distances = [int(i) for i in sys.stdin.readline().split()]
prices = [int(i) for i in sys.stdin.readline().split()]
prices = prices[:-1]
money = 0
minPrice = prices[0]
for i in range(n-1):
    price = prices[i]
    distance = distances[i]

    if minPrice < price:
        money += (distance*minPrice)
    else:
        minPrice = price 
        money += (distance*price)

print(money)