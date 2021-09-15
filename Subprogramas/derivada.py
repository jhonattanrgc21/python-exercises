# Desarrollo de funciones
def derivada(poli):
    derivada = list()
    grado = len(poli)
    for i in range(1, grado):
        derivada.append(int(poli[i]) * i)
    return derivada
    
# Entrada
poli = input().split()

# Proceso y salida
print(*(derivada(poli)))