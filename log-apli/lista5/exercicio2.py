geral = [
    {
        'nome': 'João',
        'tempos': [11.5, 10.75, 9.87],
        'esposa': 'Maria',
        'Salario': '10000',
        'medalhista': 'Sim'
    },
    {
        'nome': 'Carlos',
        'tempos': [12.5, 9.75, 9.92],
        'esposa': 'Maria',
        'Salario': '15500',
        'medalhista': 'Sim'
    },
    {
        'nome': 'José',
        'tempos': [11.35, 10.35, 9.97],
        'esposa': 'Ana',
        'Salario': '5600',
        'medalhista': 'Não'
    }
]

print('            DADOS - ATLETAS             ')
print('*=' * 30)


### ITEM A

pior_tempo = .0
nome_pior_tempo = ""
for atleta in geral:
    pior_tempo_atleta = max(atleta['tempos'])
    if pior_tempo_atleta > pior_tempo:
        pior_tempo = pior_tempo_atleta
        nome_pior_tempo = atleta['nome']

print("a) O nome e o pior tempo do atleta que possui o pior tempo entre todos")
print(f"- Nome: {nome_pior_tempo}")
print(f"- Pior tempo: {pior_tempo}")
print('*=' * 30)


# ITEM B

melhor_tempo = 1000000.0
nome_melhor_tempo = ""
esposa_melhor_tempo = ""
for atleta in geral:
    melhor_tempo_atleta = min(atleta['tempos'])
    if melhor_tempo_atleta < melhor_tempo:
        melhor_tempo = melhor_tempo_atleta
        nome_melhor_tempo = atleta['nome']
        esposa_melhor_tempo = atleta['esposa']

print("b)  O nome da esposa e o tempo do atleta que possui o melhor tempo")
print(f"- Atleta com o melhor tempo: {nome_melhor_tempo}")
print(f"- Esposa: {esposa_melhor_tempo}")
print(f"- Melhor tempo: {melhor_tempo}")
print('*=' * 30)


# ITEM C

medalhistas_olimpicos = list(filter(lambda a: a['medalhista'] == 'Sim', geral))
nomes = [a['nome'] for a in medalhistas_olimpicos]
somatorio_tempos = sum([sum(atleta['tempos']) for atleta in medalhistas_olimpicos])
media = somatorio_tempos / (3 * len(medalhistas_olimpicos))
print("c) média total de todos os tempos dos medalhistas olímpicos")
print(f"- Medalhistas olímpicos: {nomes}")
print(f"- Média de todos os seus tempos: {media}")
print('*=' * 30)


# ITEM D

maior_salario_esposa = .0
nome_maior_salario = ""
nome_esposa = ""
tempos = []
for atleta in geral:
    salario_esposa = float(atleta['Salario'])
    if salario_esposa > maior_salario_esposa:
        maior_salario_esposa = salario_esposa
        nome_esposa = atleta['esposa']
        nome_maior_salario = atleta['nome']
        tempos = atleta['tempos']

media_tempos = sum(tempos) / len(tempos)

print("d) O nome e a média dos tempos do atleta cuja esposa recebe o maior salário")
print(f"- Atleta: {nome_maior_salario}")
print(f"- Esposa: {nome_esposa}")
print(f"- Salario da esposa: {maior_salario_esposa}")
print(f"- Tempos do atleta: {tempos}")
print(f"- Média dos tempos: {media_tempos}")
print('*=' * 30)


# ITEM E

menor_salario_esposa = 1000000.0
nomes_casal_menor_salario = []

for atleta in geral:
    salario_esposa = float(atleta['Salario'])
    if salario_esposa < menor_salario_esposa:
        menor_salario_esposa = salario_esposa
        nomes_casal_menor_salario = [atleta['nome'], atleta['esposa']]

print("e) Os nomes do casal cuja esposa recebe o pior salário")
print(f"- Menor salario: {menor_salario_esposa}")
print(f"- Nomes do casal: {nomes_casal_menor_salario}")
print('*=' * 30)


# ITEM F

lista_salarios = [float(atleta['Salario']) for atleta in geral]
somatorio_salarios = sum(lista_salarios)

print("f) O somatório dos salários das esposas de todos os atletas")
print(f"- Salários: {lista_salarios}")
print(f"- Somatório: {somatorio_salarios}")
print('*=' * 30)


# ITEM G

dados_nao_medalhistas = [{
    'nome': atleta['nome'],
    'melhor_tempo': min(atleta['tempos']),
    'pior_tempo': max(atleta['tempos'])
} for atleta in list(filter(lambda a: a['medalhista'] == 'Não', geral))]

print("g) O melhor e o pior tempo dos não-medalhistas olímpicos")
[print(nao_medalhista) for nao_medalhista in dados_nao_medalhistas]
print('*=' * 30)


# ITEM H

### ITEM A

total_soma_letras = 0
nomes_casal_maior_soma = []
for atleta in geral:
    soma_letras = len(atleta['nome']) + len(atleta['esposa'])
    if soma_letras > total_soma_letras:
        total_soma_letras = soma_letras
        nomes_casal_maior_soma = [atleta['nome'], atleta['esposa']]

print("h) Os nomes do casal que possui a maior quantidade de letras somadas nos seus nomes")
print(f"- Nomes do casal: {nomes_casal_maior_soma}")
print(f"- Quantia de letras: {total_soma_letras}")
print('*=' * 30)
