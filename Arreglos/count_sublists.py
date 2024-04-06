def main():
    n = int(input())
    a = input().split()
    
    m = int(input())
    b = input().split()
    
    count = 0
    for i in range(m - n + 1):
        if b[i:i + n] == a:
            count += 1

    print(count)

if __name__ == '__main__':
    main()