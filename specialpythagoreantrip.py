def findtrip():
    for a in range(1, 1000):
        for b in range(a+1, 1000):
            if a**2 + b**2 == (1000-a-b)**2:
                return [a, b]
    return 0

print(findtrip())
