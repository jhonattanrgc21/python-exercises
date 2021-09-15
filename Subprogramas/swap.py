# Declaracion de operaciones
def swap(a, b):
    ''' Recibe dos elementos y los intercambia '''
    aux = a
    a = b
    b = aux
    return (a, b)

def main():
    ''' Cuerpo principal '''

    # Entrada
    a = input('Ingrese el valor de a: ')
    b = input('Ingrese el valor de b: ')

    # Proceso
    print('Antes: a = {}, b = {}'.format(a, b))
    a, b = swap(a, b)

    # Salida
    print('Antes: a = {}, b = {}'.format(a, b))
if __name__ == '__main__':
    main()