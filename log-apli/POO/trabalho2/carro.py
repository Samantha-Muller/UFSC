class Carro:
    def __init__(self, consumo):
        self.consumo = consumo
        self.combustivel = 0

    def andar(self, distancia):
        gastoCombustivel = distancia / self.consumo
        if gastoCombustivel > self.combustivel:
            raise RuntimeError(f"Carro sem combustivel suficiente para andar {distancia} Km")
        self.combustivel -= gastoCombustivel

    def obterGasolina(self):
        return self.combustivel

    def adicionarGasolina(self, litros):
        self.combustivel += litros