import sys

n = int(input())

club = dict()
for _ in range(n):
    age, name = sys.stdin.readline().split()
    age = int(age) # age를 int로 안 바꾸고 dict를 만들면 뒤에서 sort할 때 잘못 되는듯. 이거 안 하고 내서 틀림.
    if age in club.keys():
        club[age].append(name)
    else:
        club[age] = [name]

club_keys = list(club.keys())
club_keys.sort()
sorted_club = {i: club[i] for i in club_keys}
#print(sorted_club)

for i in range(len(club_keys)):
    for j in range(len(sorted_club[club_keys[i]])):
        print(club_keys[i], sorted_club[club_keys[i]][j])