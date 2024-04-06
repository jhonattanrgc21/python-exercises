def main():
    text = input()
    new_text = [letter for letter in text if letter.isdigit()]
    
    print(*new_text, sep="")

if(__name__ == '__main__'):
    main()