while True:
    try:
        numero = int(input("Digite um número: "))
        break
    except ValueError:
        print("Por favor, digite um número inteiro")

print(f"{numero} é {'Par' if numero%2==0 else 'Ímpar'}")