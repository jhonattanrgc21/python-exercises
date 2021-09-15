# Modulos
import random

# Declaracion de constantes
IMAGES = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']

WORDS = [
    'lavadora',
    'secadora',
    'sofa',
    'gobiernos',
    'diputado',
    'democracia',
    'computadora',
    'teclado'
]

# Cuerpo principal
def main():
    word = random_word()
    hidden_word = ['-'] * len(word)
    tries = 0

    while True:
        display_board(hidden_word, tries)
        current_letter = str(input('Ingrese una letra: '))

        # Si la lentra ingresada es correcta, se guardan las posiciones
        # donde se encuentra ubicada en la palabra
        letter_indexs = []
        for id in range(len(word)):
            if word[id] == current_letter:
                letter_indexs.append(id)

        # Si la letra no exisrte en la palabra se aumentan la cantidad
        # de intentos fallidos y en caso contrario, se muestran las letras
        # desbloqueadas en la palabra secreta
        if len(letter_indexs) == 0:
            tries += 1

            if tries == 7:
                display_board(hidden_word, tries - 1)
                print('')
                print('!Perdiste! la palabra correcta era: {}' .format(word))
                break
        else:
            for id in letter_indexs:
                hidden_word[id] = current_letter

            letter_indexs.clear()

        # Si ya no existen - en la palabra, se gana el juego
        try:
            hidden_word.index('-')
        except ValueError:
            print('')
            print('!Ganaste! la palabra correcta era: {}' .format(word))
            break

# Declaracion de operaciones
def random_word():
    '''
        Esta funcion permite obtener una variable
        aleatoria de la lista constante WORDS
    '''
    id = random.randint(0, len(WORDS) - 1)
    return WORDS[id]

def display_board(hidden_word, tries):
    '''
        Esta funcion permite imprimir el tablero
        y la la palabra que se esta tratando de adivinar
    '''
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('--- * --- * --- * --- * --- * --- *')

if __name__ == '__main__':
    print('B I E N V E N I D O S  A  A H O R C A D O S')
    main()
