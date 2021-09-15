# Desarrollo de la funcion
def mostrar(matriz):
    global filas # Cantidad de filas leidas como entrada

    for i in range(filas):
        print(*matriz[i])

# Variable matriz
matriz = list()

# Los ciclos while validan la cantidad de filas y columnas
while True:
    filas = int(input('Ingrese el numero de filas: '))
    if filas > 0:
        break
    else:
        print('Error, la cantidad debe ser mayor a cer\n.')

while True:
    cols = int(input('Ingrese el numero de columnas: '))
    if cols > 0:
        break
    else:
        print('Error, la cantidad debe ser mayor a cer\n.')

# Proceso
for i in range(filas):
    matriz.append(list())
    for j in range(cols):
        matriz[i].append(input('valor [%d, %d]: ' % (i + 1, j + 1))) 

# Salida
mostrar(matriz)