a = int(input())
b = int(input())

for i in range(a, b+1):
    if i > 1:
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            print(i)