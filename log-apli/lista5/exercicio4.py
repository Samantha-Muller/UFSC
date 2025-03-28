matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o elemento [{l + 1}][{c + 1}]: '))

print("Sua matriz: ")
[print(linha) for linha in matriz]

matriz_transposta = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(0, 3):
    for j in range(0, 3):
        matriz_transposta[j][i] = matriz[i][j]

print("Matriz transposta: ")
[print(linha) for linha in matriz_transposta]
