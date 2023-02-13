n, m = map(int, input().split())

lst_a, lst_b = [], []
for i in range(n):
    lst_a.append(list(map(int, input().split())))
for j in range(n):
    lst_b.append(list(map(int, input().split())))

for i in range(n):#len(lst_a)):
    lt_a = lst_a[i]
    lt_b = lst_b[i]
    for j in range(m): #len(lt_a)):
        print(lt_a[j] + lt_b[j], end=' ')
        #if j < len(lt_a) - 1:
        #    print(lt_a[j] + lt_b[j], end=' ')
        #else:
        #    print(lt_a[j] + lt_b[j])

