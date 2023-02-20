import sys

n = int(input())

coord = list(map(int, sys.stdin.readline().split()))
coord_set = list(set(coord))
coord_set.sort()
#print(coord_set)

# for i in range(n):
#     print(coord_set.index(coord[i]), end=' ')
# 이렇게 풀면 시간 초과 뜸

# 아래와 같이 풀어야 함 -> 딕셔너리가 빠르잖아. 잘 활용해보자.
compress = {coord_set[i]: i for i in range(len(coord_set))}
#print(compress)

for num in coord:
    #print(num)
    print(compress[num], end=' ')
