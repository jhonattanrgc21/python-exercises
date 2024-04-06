def main():
    try:
        n = int(input('Ingrese un numero entero positivo: '))
        
        if(n < 0):
            print('Error, el numero debe ser positivo.')
        elif n == 0 or n == 1:
            fib = n
        else:
            fib = 0
            ant = 0
            act = 1
            for i in range(2, n + 1):
                fib = (ant + act)
                ant = act
                act = fib
            print('Fibonacci de {} = {}'.format(n, fib))
    except ValueError:
        print('Error. debe ingresar un numero entero.')

if __name__ == '__main__':
    main()