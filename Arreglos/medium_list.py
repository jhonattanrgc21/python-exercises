def main():
    cases = int(input())
    for case in range(cases):
        n = int(input())
        array = list(map(int, input().split()))
        array.sort()
        
        valor_medio = n // 2

        cola_1 = array[:valor_medio]
        cola_2 = array[valor_medio:]
        print(' '.join([str(valor) for valor in cola_1]))
        print(' '.join([str(valor) for valor in cola_2]))
        
        array.clear()

if __name__ == '__main__':
    main()