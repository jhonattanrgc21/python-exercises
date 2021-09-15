# Entrada
while True:
    fecha = int(input("Ingrese el año: "))
    if fecha > 0:
        break

# Proceso y salida
if fecha % 4 == 0 or (fecha % 100 == 0 and fecha % 400 == 0):
    print("%d es bisiesto" % fecha)
else: 

    print("%d no es bisiesto" % fecha)