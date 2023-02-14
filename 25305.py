n, k = map(int, input().split())
lst_x = list(map(int, input().split()))

lst_x.sort()
#print(lst_x)
cut = lst_x[n-k]
print(cut)
