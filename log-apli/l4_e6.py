#!/usr/bin/python

alunos = []
melhorAluno = ["", 0.0, 0.]
for alunoNumero in range(5):
    nome = input(f"Digite o nome do aluno ({alunoNumero + 1}): ")
    media = float(input(f"Digite a media geral ({alunoNumero + 1}): "))
    valorMensalidade = float(input(f"Digite o valor da mensalidade ({alunoNumero + 1}): "))
    alunos.append([nome, media, valorMensalidade])

for aluno in alunos:
    if aluno[1] > melhorAluno[1]:
        melhorAluno = aluno

desconto = melhorAluno[2] * 0.3

print(f"Aluno com melhor media: {melhorAluno[0]}")
print(f"Media do melhor aluno: {melhorAluno[1]}")
print(f"Valor da mensalidade (sem desconto): {melhorAluno[2]}")
print(f"Valor da mensalidade (com desconto): {melhorAluno[2] - desconto}")


