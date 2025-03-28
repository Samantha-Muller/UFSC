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
