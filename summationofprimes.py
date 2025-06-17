import math

def isprime(n):
    if n<2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n%i==0:
            return False
    return True

sum = 0
for i in range(1, 2000000):
    if isprime(i):
        sum += i
print(sum)
    