def main():
    cad = input()
    is_palindromo = lambda cad: cad.lower() == cad.lower()[::-1]
    print(is_palindromo(cad))

if(__name__ == '__main__'):
    main()