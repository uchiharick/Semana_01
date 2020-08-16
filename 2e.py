altura = float(input("Altura: "))
comprimento = float(input("Comprimento: "))
largura = float(input("Largura: "))

area_piso = largura * comprimento
volume_da_sala = largura * comprimento * altura
area_das_paredes_da_sala = (2 * altura) * (largura + 2) * (altura * comprimento)

print(f'{area_piso}')
print(f'{volume_da_sala}')
print(f'{area_das_paredes_da_sala}')