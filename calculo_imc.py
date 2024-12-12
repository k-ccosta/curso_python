nome = input("Digite seu nome: ")
altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em kg: "))

imc = peso/(altura**2)

if imc < 18.5:
    categoria = "abaixo do peso"
elif imc < 24.9:
    categoria = "peso normal"
elif imc < 29.9:
    categoria = "sobrepeso"
elif imc < 34.9:
    categoria = "obesidade grau I"
elif imc < 39.9:
    categoria = "obesidade grau II"
else:
    categoria = "obesidade grau III ou mórbida"

print(f"{nome} tem {altura} de altura, pesa {peso} kg e seu IMC é {imc:.2f} | {categoria}")
