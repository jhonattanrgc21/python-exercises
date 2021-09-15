def readN():
    ''' Lee y valida la cantidad de
        numeros a solicitar '''
    while True:
        try:
            n = int(input('Ingrese el valor de N: '))
            if n > 0: break
            else: print('Error, el valor debe ser mayor a cero!')
        except: print('Error, solo puede ingresar nueros!')
    return n

def fill(array, n):
    ''' Almacena N numeros enteros
        en la lista array '''
    for i in range(n):
        array.append(int(input('Valor {}: '.format(i + 1))))

def add(array, n):
    ''' Rtorna la suma de los numeros
        pares e impares '''
    even = 0
    odd = 0
    for i in range(n):
        if array[i] % 2 == 0: even += array[i]
        else: odd += array[i]
    return even, odd

def main():
    ''' Cuerpo principal '''
    # Entrada
    n = readN()
    array = []
    fill(array, n)

    # Proceso
    even, odd = add(array, n)

    # Salida
    print('Suma de numeros pares: {}\nSuma de numeros impares: {}'.format(even, odd))
    array.clear()

if __name__ == '__main__':
    main()