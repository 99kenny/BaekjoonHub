coinNum, amount = input().split()
coinNum = int(coinNum)
amount = int(amount)
value = []

for i in range(0,coinNum):
    value.append(int(input()))

count = 0
value.reverse()

for i in value:
    count += (amount // i)
    amount = amount % i
print(count)        