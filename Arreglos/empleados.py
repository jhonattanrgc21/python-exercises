# Declaracion de operaciones
def readN():
    ''' Solicita la cantidad de emplados al usuario '''
    while True:
        try:
            n = int(input('Ingrese el numero de empleados: '))
            if n > 0:
                break
            else:
                print('Error, no puede ingresar numeros negativs.')
        except:
            print('Error, solo puede ingresar numeros.')

    return n

def netPlay(n):
    ''' Calcula el pago neto de cada mpleado '''
    a = list()
    b = list()
    c = list()
    t = list()

    for i in range(n):
        print('Empleado %d' % (i + 1))
        a.append(float(input('Sueldo: ')))
        b.append(float(input('Asignaciones: ')))
        c.append(float(input('Deducciones: ')))
        t.append(a[i] + b[i] - c[i])
        print('\n')

    a.clear()
    b.clear()
    c.clear()
    return t

def main():
    ''' Cuerpo principal '''

    # Entrada
    t = list()
    n = readN()

    # Proceso
    t = netPlay(n)

    # Salida
    for i in range(n):
        print('Total a pagar al empleado {}: {:.2f}'.format(i + 1, t[i]))

    t.clear()

if __name__ == '__main__':
    main()
