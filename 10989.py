import sys

SIZE = 10000

def counting_sort(count, n):
    #output = [0] * n

    k = 0
    for j in range(SIZE): #sum(count)):
        while count[j] != 0:
            print(j + 1)
            count[j] -= 1
            k += 1

n = int(input())

count = [0] * SIZE
for  _ in range(n):
    count[int(sys.stdin.readline())-1] += 1

counting_sort(count, n)

