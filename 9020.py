# find prime number between a and b
def get_prime_ab(a, b):
    if a == 0 and b == 0:
        return None
    primes = get_prime_list(b)
    primes = [x for x in primes if x > a and x <= b]

    return primes


def get_prime_list(n):
    a = [False,False] + [True]*(n-1)
    primes=[]

    for i in range(2,n+1):
      if a[i]:
        primes.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False
    return primes

# get_subsets로 풀면 시간 초과 뜸
'''
def get_subsets(lst, sum_):
    subset = []
    diff = 10000
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] + lst[j] == sum_ and abs(lst[i]-lst[j]) < diff:
                diff = abs(lst[i]-lst[j])
                subset = [lst[i], lst[j]]
    return subset'''

t = int(input())
for _ in range(t):
    n = int(input())
    primes = get_prime_ab(0, n)
    #print(primes)
    #subset = get_subsets(primes, n)
    #print(subset)  
    tmp = n // 2
    if (tmp in primes) and ( (n-tmp) in primes ):
        print(tmp, n - tmp)
    else:
        #print('hello')
        while (tmp not in primes) or ( (n-tmp) not in primes ):
            #print('hello 2')
            #print(tmp, n-tmp, primes)
            tmp -= 1
        print(tmp, n - tmp)
