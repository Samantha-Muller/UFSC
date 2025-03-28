#!/usr/bin/python

alunos = []
melhorAluno = ["", 0.0]
for alunoNumero in range(2):
    nome = input(f"Digite o nome do aluno ({alunoNumero + 1}): ")
    nota1 = float(input(f"Digite a primeira nota ({alunoNumero + 1}): "))
    nota2 = float(input(f"Digite a segunda nota ({alunoNumero + 1}): "))
    nota3 = float(input(f"Digite a terceira nota ({alunoNumero + 1}): "))
    media = (nota1 + nota2 + nota3) / 3
    alunos.append([nome, media])

for aluno in alunos:
    if aluno[1] > melhorAluno[1]:
        melhorAluno = aluno

if melhorAluno[1] >= 5.75:
    conceito = "APROVADO"
elif melhorAluno[1] >= 2.75:
    conceito = "EM RECUPERAÇÃO"
else:
    conceito = "REPROVADO"
print(f"Aluno com melhor media: {melhorAluno[0]}")
print(f"Media do melhor aluno: {melhorAluno[1]}")
print(f"Conceito: {conceito}")
