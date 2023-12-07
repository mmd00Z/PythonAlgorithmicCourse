a, b, c = list(map(int, input().split()))

if a + b + c == 180 and a * b * c != 0:
    print('Yes')
else:
    print('No')