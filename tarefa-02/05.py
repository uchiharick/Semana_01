#função para pagamento avista
def avista(valor):
    #processamento dos dados
    return valor - (valor * (9 / 100))

#função para pagamento divido em 5x sem juros
def pagamento_5_vezes(valor):
    #processamento dos dados
    return valor / 5

#função para pagemento divido em 10x com juros de 17%
def pagamento_10_vezes(valor):
    #processamento dos dados
    return (valor + (valor * (17 / 100))) / 10

# função principal
def main():

    #Entrada de dados
    valorCompra = int(input())

    #Saída dos dados 
    print(avista(valorCompra))
    print(pagamento_5_vezes(valorCompra))
    print(pagamento_10_vezes(valorCompra)) 


if __name__ == "__main__" :
    main()