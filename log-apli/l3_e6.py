#!/usr/bin/python

nota1 = float(input("Digite a nota 1: "))
if nota1 > 10.0 or nota1 < 0: 
    print("A nota deve ser um valor entre 0 e 10")
    exit()

nota2 = float(input("Digite a nota 2: "))
if nota2 > 10.0 or nota2 < 0:
    print("A nota deve ser um valor entre 0 e 10.0")
    exit()

media = (nota1 + nota2)/2

if media >= 9.0 and media <= 10.0:
    conceito = "A"
elif media >= 7.5 and media <= 9.0:
    conceito = "B"
elif media >= 6.0 and media <= 7.5:
    conceito = "C"
elif media >= 4.0 and media <= 6.0:
    conceito = "D"
elif media >= 0 and media <= 4.0:
    conceito = "E"

print(f"A sua média é: {media:.1f}")
print(f"Seu conceito é: {conceito}")
