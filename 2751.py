import sys

n = int(input())

lst = []
for _ in range(n):
    lst.append(int(sys.stdin.readline()))

lst.sort()

for i in range(n):
    print(lst[i])
