from Funcionario import Funcionario

lista_funcionarios = [
    Funcionario(nome="Joao", salario=1900),
    Funcionario(nome="Samantha", salario=2400),
    Funcionario(nome="Beltrano", salario=3800),
]

for funcionario in lista_funcionarios:
    print("="*15)
    print(f"Nome do funcionario: {funcionario.nome}")
    print(f"Salario: R$ {funcionario.salario}")
    print(f"Aumento: R$ {funcionario.calcularAumento()} ({funcionario.taxaAumentoSalario()*100}%)")
    print(f"Salario reajustado: R$ {funcionario.salario_reajustado}")
    print("="*15)

