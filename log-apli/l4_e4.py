#!/usr/bin/python

numeroPessoas = int(input("Digite o número de alunos na turma: "))
if numeroPessoas <= 0:
    print("ERRO: número de pessoas deve ser um inteiro maior que zero")
    exit()

somatorioIdades = 0
for pessoa in range(numeroPessoas):
    idade = int(input(f"Digite a idade ({pessoa + 1}): "))
    if idade <= 0:
        print("ERRO: idade deve ser um inteiro maior que zero")
        exit()
    somatorioIdades = somatorioIdades + idade

mediaIdade = somatorioIdades / numeroPessoas
print(f"A media das idades da turma é de {mediaIdade:.2f}")

if mediaIdade <= 25:
    categoria = "jovem"
elif mediaIdade <= 60:
    categoria = "adulta"
else:
    categoria = "idosa"

print(f"Categoria da turma: {categoria}")
