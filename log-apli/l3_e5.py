#!/usr/bin/python

valorHora = int(input("Digite o valor da hora de trabalho: "))
qtdHoras = int(input("Digite a quantidade de horas trabalhadas: "))

salarioBruto = valorHora * qtdHoras
inss = salarioBruto * 0.1
fgts = salarioBruto * 0.11

if salarioBruto <= 900:
    irPercento = 0
elif salarioBruto > 900 and salarioBruto <= 1500:
    irPercento = 0.05
elif salarioBruto > 1500 and salarioBruto <= 2500:
    irPercento = 0.1
elif salarioBruto > 2500:
    irPercento = 0.2

irDesconto = salarioBruto * irPercento

totalDesc = irDesconto + inss + fgts
salarioLiquido = salarioBruto - totalDesc

print(f"Salário Bruto: ({qtdHoras} * {valorHora}): R$ {salarioBruto:.2f}")
print(f"(-) IR ({irPercento*100}%): R$ {irDesconto:.2f}")
print(f"(-) INSS (10%): R$ {inss:.2f}")
print(f"FGTS (11%): R$ {fgts:.2f}")
print(f"Total de Descontos: R$ {totalDesc:.2f} ")
print(f"Salário Líquido: R$ {salarioLiquido:.2f}")





