#Entrada
while True:
    n = int(input("Ingrese la cantidad de notas: "))
    if n > 0:
        break
    else:
        print("Error, el numero debe ser positivo.")


# Proceso
acum = 0
for i in range(n):
    # Solicitud de notas
    nota = float(input("Nota " + str(i + 1) + ": "))
    acum += nota

# Salida
print("\nPromedio = %.2f" % (acum / n))