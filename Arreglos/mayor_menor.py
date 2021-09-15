# Entrada
l = list()
for i in range(10):
    l.append(float(input('Valor %d: ' % (i + 1))))

# Proceso y salida
mayor = max(l)
menor = min(l)
cont_mayor = l.count(mayor)
cont_menor = l.count(menor)
print('\nValor minimo: ', menor)
print('Valor maximo: ', mayor)

if cont_menor == 1:
    print('El valor minimo aparece 1 vez')
else:
    print('El valor minimo aparece %d veces' % cont_menor)

if cont_mayor == 1:
    print('El valor maximo aparece 1 vez')
else:
    print('El valor maximo aparece %d veces' % cont_mayor)

l.clear()
