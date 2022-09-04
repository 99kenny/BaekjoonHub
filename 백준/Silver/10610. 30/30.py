import sys

n = sys.stdin.readline().rstrip()
sum = 0
nums = []
for i in n:
    sum += int(i)
    nums.append(i)
if '0' not in nums or sum % 3 != 0 :
    print(-1)
else :
    nums.sort(reverse=True)
    print("".join(nums))