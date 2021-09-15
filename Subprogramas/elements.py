#  Desarrollo de funciones
def elements(n):
    """
        Determina el elemento mayor y menor
        de todos los elementos ingresados
     """
    global min_element
    global max_element

    if n < min_element:
        min_element = n

    if n > max_element:
        max_element = n


def main():
    """ Cuerpo principal """

    while True:
        # Entrada
        try:
            n = int(input('Ingrese un numero: '))
            if (n < 0):
                print('Error, el numero debe ser mayor a 0.')
        except:
            print('Error, debe ingresar un numero!')

        # Proceso
        elements(n)

        # Validando la respuesta de tried
        while True:
            tried = input('¿Desea ingresar otro elemento? (S/N): ')
            tried = tried.lower()
            if (tried != 's' and tried != 'n') or len(tried) == 0 or tried.isnumeric():
                print('Error, respuesta incorrecta.')
            else:
                break

        if tried == 'n':
            break

    # Salida
    print('Elemento menor = {}\nElemento mayor = {}'.format(
        min_element, max_element))


if __name__ == '__main__':
    min_element = 1000000000
    max_element = -1000000000
    main()
