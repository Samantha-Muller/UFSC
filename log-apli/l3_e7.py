#!/usr/bin/python

print("Isso é um interrogatório, você precisa responder a cinco perguntas sobre o assassinato do fulano de tal.")
print("Digite S para responder 'sim' e N para responder 'não'")

contador = 0

questaoA = input("Telefonou para a vítima? ")
if questaoA == "S":
    contador = contador + 1
elif questaoA != "N":
    print("Digite S ou N")
    exit()

questaoB = input("Esteve no local do crime? ")
if questaoB == "S":
    contador = contador + 1
elif questaoB != "N":
    print("Digite S ou N")
    exit()

questaoC = input("Mora perto da vítima? ")
if questaoC == "S":
    contador = contador + 1
elif questaoC != "N":
    print("Digite S ou N")
    exit()

questaoD = input("Devia para a vítima? ")
if questaoD == "S":
    contador = contador + 1
elif questaoD != "N":
    print("Digite S ou N")
    exit()

questaoE = input("Já trabalhou com a vítima? ")
if questaoE == "S":
    contador = contador + 1
elif questaoE != "N":
    print("Digite S ou N")
    exit()

if contador == 2: 
    print("Você foi clasificado como suspeito.")
elif contador == 3 or contador == 4:
    print("Você foi classificado como cúmplice. ")
elif contador == 5:
    print("Você é o assassino!")
else:
    print("Você é inocente!")
