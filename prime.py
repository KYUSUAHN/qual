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

