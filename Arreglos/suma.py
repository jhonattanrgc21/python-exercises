def main():
    ''' Cuerpo principal '''

    # Entrada
    l = list()

    while True:
        try:
            n = int(input('Ingrese el valor de N: '))
            if n > 0:
                break
            else:
                print('Error, no puede ingresar numeros negativs.')
        except:
            print('Error, solo puede ingresar numeros.')

    # Proceso
    for i in range(n):
        l.append(int(input('Numero {}: '.format(i + 1))))

    # Salida
    print('La suma de los elementos es: {}'.format(sum(l)))
    l.clear()

if __name__ == '__main__':
    main()