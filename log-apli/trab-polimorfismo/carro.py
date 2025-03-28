from ex_polimorfismo_veiculo import Veiculo


class Carro(Veiculo):
    def __init__(self, cor, marca, modelo, qtd_tanque, ano):
        super().__init__(cor, marca, modelo, qtd_tanque)
        self.ano = ano

    def imprime(self):
        print('O veículo', self.get_marca(), self.get_modelo(),
              'de cor', self.get_cor(),
              'ano', self.get_ano(),
              'tem', self.get_qtd_tanque(), 'litros no tanque')

    def get_limite_litros_tanque(self):
        return 50

    def set_ano(self, ano):
        self.ano = ano

    def get_ano(self):
        return self.ano
