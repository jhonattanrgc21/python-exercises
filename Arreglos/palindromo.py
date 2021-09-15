def main():
    """ Cuerpo principal """
    
    # Entrada
    while True:
        cad = str(input('Ingrese un texto: '))
        if len(cad) == 0:
            print('Error, la cadena no puede ser vacia.')
        else:
            break

    # Proceso
    cad_copy = cad.lower()
    palindromo = lambda cad: cad == cad[::-1]

    # Salida
    if palindromo(cad_copy):
        print('{} es palindromo'.format(cad))
    else:
        print('{} no es palindromo'.format(cad))

if __name__ == '__main__':
    main()