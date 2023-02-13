# sum: 2 3 4 5 6 ...
# 분수의 합이 2 3 4 5 6 ...
# 2이면 1번째 그룹
# 3이면 2번째 그룹
# 각 n번째 그룹 안에서 n부터 1까지 가면서 x번째 분수의 x값이 늘어남
# 그룹 당 element 개수는 1, 2, 3, 4, 5, ...
# lst_ = [1, 2, 4, 7, 11, 16, ...]

lst_ = []
x, i = 1, 1
while x <= 10000000:
    lst_.append(x)
    x += i 
    i += 1
#print(lst_[:10])

print(lst_[-3:])
val = int(input())
if val == 1:
    group = 1
    print('1/1')
else:
    if val >= lst_[-1]:
        group = len(lst_) #+ 2
        ind = val - lst_[-1]
    else: 
        group = 1
        for i in range(len(lst_)-1):
            if val >= lst_[i] and val < lst_[i+1]:
                group = i + 1
                ind = val - lst_[i] #+ 1
    
    sum_ = group + 1
    bunja = sum_ - ind - 1
    bunmo = ind + 1 
    print(str(bunja)+'/'+str(bunmo))
