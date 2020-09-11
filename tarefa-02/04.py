def cont(n1,n2,n3,n4,n5):
    maximo = max(n1,n2,n3,n4,n5)
    minimo = min(n1,n2,n3,n4,n5)

    media = (n1 + n2 + n3 + n4 + n5) / 5

    print(f'O maior número digitado foi {maximo}')
    print(f'O menor número digitado foi {minimo}')
    print(f'A média dos números foi de {media}')

def main():
    n1 = int(input('Digite o 1° numero: '))
    n2 = int(input('Digite o 2° numero: '))
    n3 = int(input('Digite o 3° numero: '))
    n4 = int(input('Digite o 4° numero: '))
    n5 = int(input('Digite o 5° numero: '))

    cont(n1,n2,n3,n4,n5)

if __name__ == "__main__" :
    main()