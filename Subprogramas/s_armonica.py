# Desarrollo de funciones
def suma(n):
    suma = 1
    for i in range(2, n + 1):
        suma += 1 / i
    return suma
# Entrada
while True:
    terna = int(input('Ingrese el valor de la terna: '))
    if terna > 0:
        break
    else:
        print('Error, el valor debe ser mayor a 0')

# Proceso y salida
print('Resultado: %.2f' % suma(terna))