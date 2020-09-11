#função de conversão dos segundos para horas, minutos, segundos
def converte(segundos):

    #Processamentos dos dados
    hora = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos = (segundos % 3600) % 60

    #Retorno do processamentos do dados dá função "converte"
    return f'{hora}H:{minutos}M:{segundos}S'

#funcão principal que irá conter os dados de entrada e as saídas do dados
def main():

    #Entradas dos dados
    segundos = int(input("Digite o total de segundos: "))
    total = converte(segundos)

    #Saída dos dados
    print(f'O fortamato dos segundos convertido ficou {total}')
    
#Verificação da função
if __name__ == '__main__':

    #Chamado da função main(principal)
    main()
