###########################################################
####################    EXERCICIO 2    ####################
###########################################################

def exercicio2():
    from aluno import Aluno

    def imprimeInfosAluno(aluno: Aluno):
        print(f"Nome do aluno: {aluno.nome}")
        print(f"Curso: {aluno.curso}")
        print(f"Tempo sem dormir: {aluno.tempoSemDormir}")

    aluno = Aluno("Fulano de Tal", "Gastronomia", 18)
    imprimeInfosAluno(aluno)

    print("Dormindo 4 horas..")
    aluno.dormir(4)
    imprimeInfosAluno(aluno)

    print("Estudando 7 horas..")
    aluno.estudar(7)
    imprimeInfosAluno(aluno)


###########################################################

###########################################################
####################    EXERCICIO 3    ####################
###########################################################

def exercicio3():
    from carro import Carro

    possante = Carro(17)

    print(f"Abastecendo 50 litros...")
    possante.adicionarGasolina(50)
    print(f"Gasolina: {possante.obterGasolina()}")

    print(f"Andando 100 Km...")
    possante.andar(100)
    print(f"Gasolina atual: {possante.obterGasolina()}")


###########################################################

exercicio3()
