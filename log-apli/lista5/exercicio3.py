matriz = [[0, 0], [0, 0]]

for l in range(0, 2):
    for c in range(0, 2):
        matriz[l][c] = int(input(f'Digite o elemento [{l + 1}][{c + 1}]: '))

print("Sua matriz: ")
[print(linha) for linha in matriz]

maior_nro = max([max(matriz[0]), max(matriz[1])])
for i in range(0, 2):
    for j in range(0, 2):
        matriz[i][j] = matriz[i][j] * maior_nro

print(f"Multiplicando matriz por maior elemento: {maior_nro}")
[print(linha) for linha in matriz]
