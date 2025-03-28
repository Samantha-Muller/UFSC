nro_tentativas = 6
segredo = "dialetica"
letras_descobertas = ["_"] * len(segredo)
print('*=' * 30)
print('            JOGO DA FORCA             ')
print('        VOCÊ TEM 6 TENTATIVAS         ')
print('*=' * 30)


while True:
    letra = str(input("Digite uma letra: "))
    if len(letra) != 1 or not letra.isalpha():
        print("Digite somente uma letra!")
        continue
    letra = letra.lower()
    if letra not in segredo:
        nro_tentativas -= 1
        if nro_tentativas == 0:
            print("Você perdeu! ENFORCADO!")
            break
        else:
            print(f"-> Você errou pela {6 - nro_tentativas} vez. Tente de novo!")
        continue
    for i in range(len(segredo)):
        if segredo[i] == letra:
            letras_descobertas[i] = letra.upper()
    palavra = ' '.join(letras_descobertas)
    print(f"A palavra é: {palavra}")
    if '_' not in letras_descobertas:
        print("Parabéns! Você venceu!")
        break
