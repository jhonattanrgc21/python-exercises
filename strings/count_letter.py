def main():
    text = input()
    letter = input()
    
    print('La letra \'{}\' se encuentra {} veces repetida.'.format(letter, text.count(letter)))

if(__name__ == '__main__'):
    main()