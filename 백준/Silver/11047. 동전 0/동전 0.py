coinNum, amount = input().split()
coinNum = int(coinNum)
amount = int(amount)
value = []

for i in range(0,coinNum):
    value.append(int(input()))

count = 0
total = amount

for i in range(0,coinNum):
    index = coinNum - i - 1
    count += (total // value[index])
    total = total % value[index]
print(count)        