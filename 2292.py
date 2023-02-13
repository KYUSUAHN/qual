lst_ = []
n, i = 1, 0
while n < 1000000000:
    i += 1
    lst_.append(n)
    n += 6 * i 
#print(lst_[:6])

val = int(input())
answer = 0
judge = []
for j in range(len(lst_)):
#    print(val, lst_[j])
    if val > lst_[j]:
#        print("plus")
        answer += 1
        judge.append('plus')
    else:
#        print("break")
        break
#print(answer)
print(len(judge)+1)
