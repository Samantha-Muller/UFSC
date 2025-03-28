def metade(valor, formatar=False):
    if formatar:
        return moeda(valor / 2)
    else:
        return valor / 2


def dobro(valor, formatar=False):
    if formatar:
        return moeda(valor * 2)
    else:
        return valor * 2


def aumentar(valor, porcentagem, formatar=False):
    if formatar:
        return moeda(valor + (valor * (porcentagem / 100)))
    else:
        return valor + (valor * (porcentagem / 100))


def diminuir(valor, porcentagem, formatar=False):
    if formatar:
        return moeda(valor - (valor * (porcentagem / 100)))
    else:
        return valor - (valor * (porcentagem / 100))


def moeda(valor):
    return f"R${valor:.2f}".replace(".", ",")


def resumo(valor, formatar=False):
    print("-"*30)
    print("RESUMO DO VALOR")
    print("-"*30)
    print(f"Preço analisado: {moeda(valor)}")
    print(f"Dobro do preço: {dobro(valor, formatar)}")
    print(f"Metade do preço: {metade(valor, formatar)}")
    print(f"80% de aumento: {aumentar(valor, 80, formatar)}")
    print(f"35% de redução: {diminuir(valor, 35, formatar)}")
    print("-"*30)






















