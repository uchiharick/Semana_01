hora = int(input('Digite a hora: '))
minuto = int(input('Digite os minutos: '))
segundo = int(input('Digite os segundos: '))

horas = (hora *  60) * 60
minutos = minuto * 60

resultado = horas + minutos + segundo

print(resultado)