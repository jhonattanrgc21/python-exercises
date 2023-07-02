def main():
    # Busca la ultima aparicion de un caracter comenzando desde el final
    cad = input()
    letter = input()
    print(cad.rfind(letter))

if(__name__ == '__main__'):
    main()