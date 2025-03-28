#!/usr/bin/python
import math


def encontra_intervalo_funcionario(vendas):
    comissao = vendas * 0.09
    indice = min(math.floor(comissao / 100), 8)
    return indice


def conta_funcionarios_intervalo(lista_funcionarios):
    # Contador dos intervalos, iniciando em 0 todas as posicoes
    contador_intervalos = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    # O intervalo da comissão é equivalente ao intervalo dos salários subtraindo 200
    intervalos_comissao = [99, 199, 299, 399, 499, 599, 699, 799]

    # Iterando sobre lista de funcionarios
    for func in lista_funcionarios:

        # Pega valor das vendas do funcionario
        vendas = func[1]
        indice = encontra_intervalo_funcionario(vendas)
        contador_intervalos[indice] = contador_intervalos[indice] + 1

    return contador_intervalos


# Função para receber funcionários
def recebe_funcionarios(numero_funcionarios):
    dados = []
    for i in range(numero_funcionarios):
        nome = input(f"Digite o nome do funcionário nº {i + 1}: ")
        valor_venda = -1.0
        while valor_venda < 0.0:
            valor_venda = float(input(f"Digite o valor das vendas do funcionário nº {i + 1}: "))
            if valor_venda < 0:
                print("O valor da venda não pode ser negativo")
        dados.append([nome, valor_venda])
    return dados


# Recebe input do usuario de quantos funcionários
#num_funcionarios = int(input("Quantos funcionarios você vai inserir? Digite um numero inteiro: "))

# Recebe funcionarios
#lista_funcionarios = recebe_funcionarios(num_funcionarios)

# Conta quantia de funcionarios em cada intervalo
#contagem_intervalos = conta_funcionarios_intervalo(lista_funcionarios)

#print(contagem_intervalos)