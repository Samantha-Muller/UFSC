#!/usr/bin/python

numInicio = int(input("Digite o numero inicial: "))
numFim = int(input("Digite o numero final: "))

if numInicio >= numFim:
    print("ERRO: numero final deve ser maior que o numero inicial")

total = 0
for numero in range(numInicio, numFim):
    print(numero)
    total = total + numero

print(f"Soma dos numeros: {total}")
