nome = input("Digite seu nome: ")
altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em kg: "))

imc = peso/(altura**2)

print(f"{nome} tem {altura} de altura, pesa {peso} kg e seu IMC é {imc:.2f}")