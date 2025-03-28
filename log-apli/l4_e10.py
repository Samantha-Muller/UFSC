#!/usr/bin/python

# Exercicio 1
anoBissexto = 2004
while anoBissexto <= 2096:
    print(anoBissexto)
    anoBissexto = anoBissexto + 4


# Exercicio 2
numeroImpar = 1
while numeroImpar < 50:
    print(numeroImpar)
    numeroImpar = numeroImpar + 2


# Exercicio 3
totalPares = 0
totalImpares = 0
indicador = 1
while indicador <= 5:
    numero = int(input(f"Digite um numero inteiro qualquer ({indicador}): "))
    if numero % 2 == 0:
        totalPares = totalPares + 1
    else:
        totalImpares = totalImpares + 1
    indicador = indicador + 1

print(f"Total de numeros pares: {totalPares}")
print(f"Total de numeros impares: {totalImpares}")


# Exercicio 4
numeroPessoas = int(input("Digite o número de alunos na turma: "))
if numeroPessoas <= 0:
    print("ERRO: número de alunos deve ser um inteiro maior que zero")
    exit()

somatorioIdades = 0
indicadorPessoa = 1
while indicadorPessoa <= numeroPessoas:
    idade = int(input(f"Digite a idade ({indicadorPessoa}): "))
    if idade <= 0:
        print("ERRO: idade deve ser um inteiro maior que zero")
        exit()
    somatorioIdades = somatorioIdades + idade
    indicadorPessoa = indicadorPessoa + 1

mediaIdade = somatorioIdades / numeroPessoas
print(f"A media das idades da turma é de {mediaIdade:.2f}")

if mediaIdade <= 25:
    categoria = "jovem"
elif mediaIdade <= 60:
    categoria = "adulta"
else:
    categoria = "idosa"

print(f"Categoria da turma: {categoria}")
