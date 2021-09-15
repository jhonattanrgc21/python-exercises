"""
    Dado un número de 4 dígitos desarrolle una función lógica que devuelva
    verdadero si el resto de dividir por diez la suma de los tres primeros 
    dígitos es igual al cuarto dígito.
"""

# Declaracion de funciones
def comparar(num):
    d4 = num % 10
    d3 = (num // 10) % 10
    d2 = (num // 10) // 10 % 10
    d1 = (num // 10) // 10 // 10
    print('{} {} {} {}' .format(d1, d2, d3, d4))
    return (d1 + d2 + d3) % 10 == d4

# Entrada
while True:
    num = int(input('Ingrese un numero de 4 digitos: '))
    if num < 1000 or num > 9999:
        print('Error, el numero debe ser de 4 digitos.')
    else: 
        break

# Proceso y salida
print(comparar(num))