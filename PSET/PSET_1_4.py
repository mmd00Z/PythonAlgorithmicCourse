l = []

tmp = int(input())

while tmp != 0:
    l.append(tmp)
    tmp = int(input())

n = len(l)

for i in range(1, n + 1):
    print(l[n - i])

l.reverse()
for i in l:
    print(i)