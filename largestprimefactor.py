def largestprimefactor(n):
    curr = 2
    last = 1

    while curr**2 <= n:
        if n % curr == 0:
            n //= curr
            last = curr
        else:
            curr += 1 if curr == 2 else 2
        
    return max(n, last)


print(largestprimefactor(600851475143))