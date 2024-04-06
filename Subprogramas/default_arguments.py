def increment_by(n, increment=1):
    return n + increment

def main():
    cases = int(input())
    for case in range(cases):
        line = input().split()
        n = int(line[1])
        salto = 2
        if line[0] == 'odd':
            size = increment_by(n, n)
            inicio = 1
        else:
            size = increment_by(n) + 1
            inicio = 0
        
        numbers = []  # Lista para almacenar los números del caso actual
        for i in range(inicio, size, salto):
            numbers.append(str(i))  # Agregar cada número a la lista como cadena
        
        # Imprimir los números del caso actual en una sola línea
        print('\n'.join(numbers))

if __name__ == '__main__':
    main()
