def cont(nome):
  return len(nome)

def main():
  usuario = str(input("Digite um nome qualquer: "))
  print(f'o total de carecteres lido foi {cont(usuario)}')

if __name__ == "__main__":
  main()
