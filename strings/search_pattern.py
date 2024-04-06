def encontrar_subcadena(cadena, subcadena):
    inicio = cadena.find(subcadena)
    if inicio == -1:
        print('(-1, -1)')
    else:
        while inicio != -1:
            fin = inicio + len(subcadena) - 1
            print('({}, {})'.format(inicio, fin))
            inicio = cadena.find(subcadena, inicio + 1)

def main():
    cad = input()
    sub_cad = input()
    encontrar_subcadena(cad, sub_cad)
    
if __name__ == '__main__':
    main()