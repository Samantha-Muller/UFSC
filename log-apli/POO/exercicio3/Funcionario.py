class Funcionario:

    def __init__(self, nome, salario):
        if salario <= 0:
            raise ValueError("Salario nao pode ser um valor negativo ou nulo!")
        self.nome = nome
        self.salario = salario
        self.salario_reajustado = salario + self.calcularAumento()

    def calcularAumento(self):
        return self.salario * self.taxaAumentoSalario()

    def taxaAumentoSalario(self):
        if self.salario <= 2000:
            return .15
        elif self.salario <= 3000:
            return .1
        else:
            return .05
