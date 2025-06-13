# _ _ _ * _ _ _


def is_palindrome(n):
    as_str = str(n)
    return as_str == as_str[::-1]


one = 100
two = 100
max = 0

for one in range(100, 1000):
    for two in range(100, 1000):
        curr = one * two
        if is_palindrome(curr) and curr > max:
            max = curr

print(max)


    
