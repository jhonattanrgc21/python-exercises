# Desarrollo de funciones
def progresion(x, n):
    """ Suma la serie de n numeros """
    acum = 0
    for i in range(n + 1):
        acum += (x**i)
    return acum

def main():
    """ Cuerpo principal """
    
    # Entrada
    while True:
        try:
            x = float(input('Ingrese el valor de X: '))
            break
        except:
            print('Error, debe ingresar un numero!')

    while True:
        try:
            n = int(input('Ingrese el valor de N: '))
            if (n > 1):
                break
            else:
                print('Error, el numero debe ser positivo.')
        except:
            print('Error, debe ingresar un numero!')

    # Proceso y salida
    print('{}^{} = {}'.format(x, n, progresion(x, n)))

if __name__ == '__main__':
    main()