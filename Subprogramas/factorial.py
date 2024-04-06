def main():
    try:
        n = int(input('Ingrese un numero: '))
        
        if n < 0:
            print('Error, debe ingresar un numero entero positivo.')
        elif n == 0 or n == 1:
            return 1
        else:
            fact = 1
            for i in range( 2, n + 1):
                fact *= i
            
        print('Factorial de {} = {}'.format(n, fact))

    except ValueError:
        print('Error, debe ingresar un número entero.')


if __name__ == '__main__':
    main()