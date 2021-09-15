# Desarrollo de funciones
def sucesion(n):
    """ Suma la serie de n numeros """
    acum = 0
    for i in range(n + 1):
        acum += i
    return acum

def main():
    """ Cuerpo principal """

    # Entrada
    while True:
        try:
            n = int(input('Ingrese un numero positivo: '))
            if (n > 0):
                break
            else:
                print('Error, el numero debe ser mayor a 0.')
        except:
            print('Error, debe ingresar un numero!')

    # Proceso y salida
    print('Suma = ', sucesion(n))

if __name__ == '__main__':
    main()