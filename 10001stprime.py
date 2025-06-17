import math

def isprime(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n%i==0:
            return False
    return True

count = 0
i = 0
while count != 10001:
    if isprime(i):
        count+=1
    i+=1

print(i-1)
