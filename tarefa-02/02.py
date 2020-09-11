# Função responsável por verificar qual número corresponde ao carecter digitado
def Unicode(caractere):

    # Retorno da Função
    return (ord(caractere))

# Função principal
def main():

    # Entrada de dados
    usuario = str(input("Digite qualquer caracter: "))

    # Saída dos dados
    print(f'o número Unicode coresponte á esse caracter é {Unicode(usuario)}')

# Verificação da Função main
if __name__ == '__main__':
    main()