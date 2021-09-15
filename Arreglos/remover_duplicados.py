# Entrada
l = list()
n = int(input('Ingrese la cantidad de elementos: '))

# Proceso
for i in range(n):
    l.append(int(input('Valor %d: ' % (i + 1))))

l.sort()
i = 0
while(i < n):
    if l[i] == l[i + 1] and (i + 1) < n:
        del(l[i])
        n -= 1
    i += 1

# Salida
print('\n', *l, sep=' ')
l.clear()