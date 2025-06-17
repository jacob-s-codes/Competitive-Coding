def collatz(n, memo={}):
    chain = 0
    orginal = n
    
    while n != 1:
        if n % 2 == 0:
            n //= 2
        n = 3*n +1
        chain += 1
    return chain

max = 0
max_num = 0
for i in range(2, 1000000):
    hold = collatz(i)
    if hold > max:
        max = hold
        max_num = i

print(max_num)