# Entrada
comparador = int(input("Ingrese el valor comparador: "))
menores = 0
mayores = 0

# Proceso
while True:
    num = int(input("Ingrese un numero: "))

    if num < comparador:
        menores += 1
    else:
        mayores += 1

    while True:
        intento = int(input("Desea ingresar otro numero? (1: Si, 2: No): "))
        if intento < 1 or intento > 2:
            print ("Error.")
        else:
            break
    
    if intento == 2:
        break

# Salida
print("\n\nMenores = %d, mayores = %d" % (menores, mayores))