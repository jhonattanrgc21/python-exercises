def verify_text(text: str):
    vocals = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    count_spaces = 0
    count_characters = 0
    
    for letter in text:
        if(letter.lower() in vocals):
            vocals[letter.lower()] += 1
        elif letter.isspace():
            count_spaces += 1
        elif not letter.isdigit() and not letter.isalpha():
            count_characters += 1
    return vocals, count_spaces, count_characters

def main():
    texto = input('Ingrese una frase: ')
    vocals, count_space, count_characters = verify_text(texto)
    print('Cantidad de caracteres: ', len(texto))
    for key, value in vocals.items():
        print('Cantidad de {}: {}'.format(key.upper(), value))
    print('Cantidad de espacios en blanco: ', count_space)
    print('Cantidad de caracteres especiales: ', count_characters)

if __name__ == '__main__':
    main()