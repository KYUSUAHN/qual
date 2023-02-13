import math

while True:
    T = int(input())
    if T == 0:
        break
    if T== 1:
        print(1)
    else:
        lists = [True]*(2*T+1)
        check = range(2, int(math.sqrt(2*T))+1)
        for i in check:
            n = 2
            while i*n <= 2*T:
                if lists[i *n]:
                    lists[i*n] = False
                n += 1
        print(sum(lists[T+1:2*T]))
