# Entrada
matriz = list()
acum = 0

while True:
    n = int(input('Ingrese la cantidad de filas: '))
    if n > 0:
        break
    else:
        print('Error, el valor debe ser mayor a cero.\n')

while True:
    m = int(input('Ingrese la cantidad de columnas: '))
    if m > 0:
        break
    else:
        print('Error, el valor debe ser mayor a cero.\n')

# Proceso
for i in range(n):
    matriz.append(list())
    for j in range(m):
        matriz[i].append(int(input('valor [%d, %d]: ' % (i + 1, j + 1)))) 
        acum += matriz[i][j]

# Salida
print('\nSuma de los elementos = ', acum)

for i in range(n):
    matriz[i].clear()

matriz.clear()