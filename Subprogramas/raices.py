# Desarrollo de funciones
def read():
    ''' Lee y valida los valores de A, B, C '''
    while True:
        try:
            a = float(input('Ingrese un valor distinto de cero para A: '))
            if a < 0:
                print('Error, el valor debe ser mayor a cero.')
                continue

            b = float(input('Ingrese el valor de B: '))
            c = float(input('Ingrese el valor de C: '))
            break
        except:
            print('Error, solo puede ingresar numeros!')
    return a, b, c

def operate(a, b, c):
    ''' Aplica la cuacion de segundo grado con A, B y C '''
    raiz = (b ** 2) - (4 * a * c)
    if raiz < 0:
        print('Error, la raiz es negativa.')
    else:
        print('x1 = {:.2f}'.format((-b + (raiz ** (1/2))) / (2 * a)))
        print('x2 = {:.2f}'.format((-b - (raiz ** (1/2))) / (2 * a)))

def main():
    # Entrada
    a, b, c = read()

    #Proceso y salida
    operate(a, b, c)

if __name__ == '__main__':
    main()