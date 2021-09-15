# Desarrollo de funciones
def read():
    ''' Lee y valida el valor de los dos numeros '''
    while True:
        try:
            a = float(input('Valor uno: '))
            b = float(input('Valor dos: '))
            break
        except:
            print('\nError, debe ingresar numeros!')
    return a, b

def menu():
    ''' Despliega un menu con las opciones de la calculadora '''
    while True:
        try:
            print('Operacion')
            print('1- Suma')
            print('2- Resta')
            print('3- Multiplicacion')
            print('4- Division')
            op = int(input('Seleccion: '))

            if op > 0 and op < 5:
                break
            else:
                print('Error, opcion invalida.\n')
        except:
            print('Error, debe ingresar numeros!')
    return op

# Funciones lambda
add = lambda a, b: a + b
substract = lambda a, b: a - b
multiply = lambda a, b: a * b
divide = lambda a, b: a / b

def show(a, b, op):
    ''' Muestra el resultado de la operacion '''
    if op == 1:
        print('\n{:.1f} + {:.1f} = {:.1f}'.format(a, b, add(a, b)))
    elif op == 2:
        print('\n{:.1f} - {:.1f} = {:.1f}'.format(a, b, substract(a, b)))
    elif op == 3:
        print('\n{:.1f} * {:.1f} = {:.1f}'.format(a, b, multiply(a, b)))
    else:
        print('\n{:.1f} / {:.1f} = {:.1f}'.format(a, b, divide(a, b)))

def main():
    ''' Cuerpo principal '''

    # Entrada
    a, b = read()

    # Proceso
    op:int = menu()

    # Salida
    show(a, b, op)

if __name__ == '__main__':
    main()
