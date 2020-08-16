def data(dia,mês,ano):
    return f'{dia}/{mês}/{ano}'

def main():
    dia = int(input('Digite o dia : '))
    mês = int(input('Digite o dia : '))
    ano = int(input('Digite o dia : '))
    print(data(dia,mês,ano))

if __name__ == "__main__" :
    main()