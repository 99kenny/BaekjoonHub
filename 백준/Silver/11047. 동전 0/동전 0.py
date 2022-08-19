coinNum, amount = input().split()
coinNum = int(coinNum)
amount = int(amount)
value = []

for i in range(0,coinNum):
    value.append(int(input()))

count = 0
total = amount
value.reverse()

for i in value:
    count += (total // i)
    total = total % i
print(count)        