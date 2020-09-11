def calculo():
    hora = int(input())
    minuto = int(input())
    segundo = int(input())

    horas = (hora *  60) * 60
    minutos = minuto * 60

    return horas + minutos + segundo

def main():
    print(calculo())

if __name__ == '__main__' :
    main()