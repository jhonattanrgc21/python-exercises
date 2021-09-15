casos = int(input())

for i in range(casos):
    n = int(input())
    a = list()
    for j in range(n):
        e = int(input())
        a.insert(0, e)
    print(*a, sep=' ')
    a.clear()