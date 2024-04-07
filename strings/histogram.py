def main():
    frase = input('Ingrese una frase: ')
    
    count_a = 0
    count_e = 0
    count_i = 0
    count_o = 0
    count_u = 0
    for letra in frase:
        if letra.lower() == 'a':
            count_a += 1
        elif letra.lower() == 'e':
            count_e += 1
        elif letra.lower() == 'i':
            count_i += 1
        elif letra.lower() == 'o':
            count_o += 1
        elif letra.lower() == 'u':
            count_u += 1
            
    print('A: ' + ('*' * count_a  ))
    print('E: ' + ('*' * count_e  ))
    print('I: ' + ('*' * count_i  ))
    print('O: ' + ('*' * count_o  ))
    print('U: ' + ('*' * count_u  ))

if __name__ == '__main__':
    main()