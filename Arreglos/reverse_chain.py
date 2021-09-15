def main():
    """ Cuerpo principal """
    
    # Entrada
    cad = str(input('Ingrese un texto: '))

    # Proceso
    cad = cad.capitalize() # Formatea la cadena para que la primera letra sea mayuscula
    print('Ahora: {}'.format(cad))
    inverse_chain = lambda cad: cad[::-1]

    # Salida
    print('Ahora: {}'.format(inverse_chain(cad)))

if __name__ == '__main__':
    main()