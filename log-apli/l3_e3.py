#!/usr/bin/py

########
#######
### EXERCICIO 3
# Essas linhas equivalem ao DECLARAR e LER
peso = int(input("Digite o peso: "))
altura = float(input("Digite a altura: "))

IMC = peso / (altura * altura)
print(f"Seu IMC é {IMC:.2f}")

if IMC < 18.5:
    print("Abaixo do peso")
elif IMC > 18.5 and IMC <= 25:
    print("Peso ideal")
elif IMC > 25 and IMC <= 30:
    print ("Sobrepeso")
elif IMC > 30 and IMC <= 40:
    print ("Obesidade")
elif IMC > 40:
    print ("Obesidade mórbida")


