import sys

def radix_sort(l):
    d = 50
    for i in range(len(l)):
        l[i] = "`"*(d-len(l[i]))+l[i]
    for r in range(d):
        m = d - r - 1
        c = [0] * 27
        for i in l:
            key = ord(i[m]) - 96
            c[key] += 1
        for j in range(1, 27):
            c[j] = c[j-1] + c[j]
        n = len(l)
        t = [0] * n
        for i in range(n-1, -1, -1):
            key = ord(l[i][m]) - 96
            t[c[key]-1] = l[i]
            c[key] = c[key] - 1
        for i in range(n):
            l[i] = t[i]
    for i in range(n):
        l[i] = l[i].replace("`","")
    return l

n = int(input())
lst = []
for _ in range(n):
    word = sys.stdin.readline().split('\n')[0]
    lst.append(word)

lst = list(set(lst))
lst = radix_sort(lst)
#print(">>>>>>>>>>>", lst)

for i in range(len(lst)):
    print(lst[i])
