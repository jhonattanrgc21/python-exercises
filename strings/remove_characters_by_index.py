def main():
    text = input().split()
    init_index = int(input())
    count = int(input())
    size = len(text)
    while(True):
        if(count > 0 and len(text) > 0):
            count -= 1
            del text
        else:
            break
    sub_text = text[init_index::count + 1]
    print(sub_text)
    
if(__name__ == '__main__'):
    main()