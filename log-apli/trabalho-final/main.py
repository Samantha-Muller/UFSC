########################################################################################
################ SEÇÃO  DE INICIALIZAÇÃO (INJEÇÃO DE DEPENDENCIAS) #####################
########################################################################################


from application.MatriculaService import MatriculaService
from application.use_cases.AtualizarCadastro import AtualizarCadastro
from application.use_cases.BuscaCadastro import BuscaCadastro
from application.use_cases.DeletarCadastro import DeletarCadastro
from application.use_cases.InserirCadastro import InserirCadastro
from infrastructure.persistence.InMemoryEstudanteRepository import InMemoryEstudanteRepository
from infrastructure.persistence.InMemoryProfessorRepository import InMemoryProfessorRepository
from infrastructure.persistence.InMemoryTecnicoAdministrativoRepository import InMemoryTecnicoAdministrativoRepository


def get_repos():
    return {
        "estudantesRepo": InMemoryEstudanteRepository(),
        "professoresRepo": InMemoryProfessorRepository(),
        "taesRepo": InMemoryTecnicoAdministrativoRepository()
    }


def get_use_cases():
    repos = get_repos()
    return {
        "atualizarCadastro": AtualizarCadastro(**repos),
        "buscaCadastro": BuscaCadastro(**repos),
        "deletarCadastro": DeletarCadastro(**repos),
        "inserirCadastro": InserirCadastro(**repos)
    }


def get_service():
    use_cases = get_use_cases()
    return MatriculaService(**use_cases)


########################################################################################
########################################################################################
####################### EXEMPLOS DE USO ABAIXO #########################################
########################################################################################
########################################################################################

import datetime

from domain.entity.Estudante import Estudante
from domain.entity.Utils import Perfil

matriculaService = get_service()

### TESTANDO FUNCIONALIDADES DE ESTUDANTE
print(50 * "#")
print("ESTUDANTES MATRICULADOS NO CURSO DE HISTÓRIA")
print(50 * "#")
for estudante in matriculaService.buscaCadastro.listarAlunosCurso("História"):
    print(f"Nome: {estudante.get_nome()}")
    print(f"Matricula: {estudante.get_matricula()}")

print(50 * "#")
print("MATRICULANDO NOVO ESTUDANTE NO CURSO DE C.I.")
print(50 * "#")
novoEstudante = Estudante(
    nome="Novo Aluno",
    matricula="8881234",
    email="ahacker@proton.me",
    cpf="013.244.290-62",
    dataNascimento=datetime.datetime(day=12, month=4, year=1988),
    curso="Ciência da Informação",
)
matriculaService.inserirCadastro.matricularEstudante(novoEstudante)

print(50 * "#")
print("ESTUDANTES MATRICULADOS NO CURSO DE C.I.")
print(50 * "#")
for estudante in matriculaService.buscaCadastro.listarAlunosCurso("Ciência da Informação"):
    print(f"Nome: {estudante.get_nome()}")
    print(f"Matricula: {estudante.get_matricula()}")

print(50 * "#")
print("TRANSFERINDO ALUNO SAMANTHA PARA C.I.")
print(50 * "#")
matricula = input("Digite a matricula a transferir")
matriculaService.atualizarCadastro.transferirAlunoDeCurso(matricula, "Ciência da Informação")

print(50 * "#")
print("ESTUDANTES MATRICULADOS NO CURSO DE HISTÓRIA")
print(50 * "#")
for estudante in matriculaService.buscaCadastro.listarAlunosCurso("História"):
    print(f"Nome: {estudante.get_nome()}")
    print(f"Matricula: {estudante.get_matricula()}")

print(50 * "#")
print("ESTUDANTES MATRICULADOS NO CURSO DE C.I.")
print(50 * "#")
for estudante in matriculaService.buscaCadastro.listarAlunosCurso("Ciência da Informação"):
    print(f"Nome: {estudante.get_nome()}")
    print(f"Matricula: {estudante.get_matricula()}")

print(50 * "#")
print("DELETANDO ALUNO LENNON")
print(50 * "#")
matriculaService.deletarCadastro.deletar(Perfil.ESTUDANTE, "2040805")

print(50 * "#")
print("ESTUDANTES MATRICULADOS NO CURSO DE HISTÓRIA")
print(50 * "#")
for estudante in matriculaService.buscaCadastro.listarAlunosCurso("História"):
    print(f"Nome: {estudante.get_nome()}")
    print(f"Matricula: {estudante.get_matricula()}")
