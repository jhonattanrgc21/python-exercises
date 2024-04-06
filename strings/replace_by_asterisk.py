def main():
    text = input().split()
    new_text = []
    for word in text:
        if len(word) == 4:
            new_text.append('****')
        else:
            new_text.append(word)
    
    #print(*new_text, sep=" ")
    print(' '.join(new_text))

if(__name__ == '__main__'):
    main()