import sys

n = int(input())

lst = []
count = [0] * 8001
for _ in range(n):
    value = int(sys.stdin.readline())
    lst.append(value)
    count[value+4000] += 1

lst.sort()

max_count = max(count)
ind, mode = [], []
for i in range(len(count)):
    if count[i] == max_count:
        mode.append(i)

if len(mode) == 1:
    mode = mode[0] - 4000
else:
    mode = mode[1] - 4000

mean = int(round(sum(lst) / n, 0))
median = lst[ (n+1)//2 - 1]
range_ = max(lst) - min(lst)

print(mean)
print(median)
print(mode)
print(range_)

