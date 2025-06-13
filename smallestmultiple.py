# num = 2520
# works = True

# while True:
#     works = True
#     for i in range(2, 21):
#         if num % i != 0:
#             works = False
#             break
#     if not works:
#         num += 1
#     else:
#         break

# print(num)

import math

def lcm(a, b):
    return (a*b)//math.gcd(a, b)

num = 1
for i in range(2, 21):
    num = lcm(num, i)

print(num)