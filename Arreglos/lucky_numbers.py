def main():
    m = int(input())
    n = int(input())
    
    numeros = list(range(1, n + 1))
    print(' '.join(str(elem) for elem in numeros))
        
    for posicion in range(2, m + 1):
        numeros_aux = numeros[::posicion]
        for numero in numeros_aux:
            numeros.remove(numero)
        print(' '.join(str(elem) for elem in numeros))

if __name__ == '__main__':
    main()