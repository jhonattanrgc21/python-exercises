# Deaarrollo de funciones
def digit(a):
    if a == '0' or a == '1' or a == '2' or a == '3' or a == '4' or a == '5' or a == '6' or a == '7' or a == '8' or a == '9':
        return True
    else:
        return False

def main():
    # Entrada
    while True:
        letter = input('Ingrese un caracter: ')
        if len(letter) < 2:
            break
        else:
            print('Error, debe ingresar un solo caracter.')

    # Proceso y salida
    if digit(letter):
        print('El caracter ingresado es un digito entre 0 y 9')
    else:
        print('El caracter ingresado no es un digito entre 0 y 9')


if __name__ == '__main__':
    main()