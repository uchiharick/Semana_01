def cubo(x):
    return x ** 3 

def main():
    numero = (int(input("Digite um número: ")))
    valor = cubo(numero)
    print(valor)

if __name__ == "__main__" :
    main()