def calculo():
    altura = int(input())
    comprimento = int(input())
    largura = int(input())

    area_piso = largura * comprimento
    volume_da_sala = largura * comprimento * altura
    area_das_paredes_da_sala = (2 * altura * largura) + (2 * altura * comprimento)

    
    print(area_piso)
    print(volume_da_sala)
    print(area_das_paredes_da_sala)

def main():  
    calculo()

if __name__ == '__main__' :
    main()
