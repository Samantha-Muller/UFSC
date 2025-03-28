from ex_polimorfismo_veiculo import Veiculo
from carro import Carro

civic = Veiculo('prata', 'Honda', 'Civic', 70)
civic.abastecer(20)
civic.abastecer(40)
civic.imprime()

hb20 = Carro('vermelho', 'Hyunday', 'HB20', 30, 2012)
hb20.abastecer(5)
hb20.abastecer(15)
hb20.imprime()
hb20.ano = 11

clio = Carro('preto', 'Renault', 'Clio', 12, 2020)
clio.abastecer(1000)
clio.imprime()



