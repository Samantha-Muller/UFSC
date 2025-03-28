from Numero import Numero

numero_input = int(input("Digite um numero inteiro"))
obj_numero = Numero(valor = numero_input)
print(f"Cubo do numero {obj_numero.valor}: {obj_numero.potencia(3)}")
