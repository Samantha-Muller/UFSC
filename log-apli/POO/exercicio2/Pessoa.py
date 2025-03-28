class Pessoa:
    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso

    def atualizarNome(self, novo_nome):
        self.nome = novo_nome

    def atualizarIdade(self, nova_idade):
        self.idade = nova_idade

    def atualizarPeso(self, novo_peso):
        self.peso = novo_peso
