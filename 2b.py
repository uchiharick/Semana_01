def media(a,b,c):
    return (a + b + c) / 3

def main():
    a = int(input('Digite um número: '))
    b = int(input('Digite um número: '))
    c = int(input('Digite um número: '))

    total = media(a,b,c)
    print(total)

if __name__ == "__main__" :
    main()