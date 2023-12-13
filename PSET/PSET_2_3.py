n = int(input())

print(n * '*')
print(((n-2) * ('*' + (n-2) * ' ' + '*\n')), end='')
print(n * '*')