from domain.entity.Estudante import Estudante
from domain.entity.Professor import Professor
from domain.entity.TecnicoAdministrativo import TecnicoAdministrativo
from domain.repository.IEstudanteRepository import IEstudanteRepository
from domain.repository.IProfessorRepository import IProfessorRepository
from domain.repository.ITecnicoAdministrativoRepository import ITecnicoAdministrativoRepository


class InserirCadastro:
    def __init__(self,
                 estudantesRepo: IEstudanteRepository,
                 professoresRepo: IProfessorRepository,
                 taesRepo: ITecnicoAdministrativoRepository,
                 ):
        self.estudantesRepo = estudantesRepo
        self.professoresRepo = professoresRepo
        self.taesRepo = taesRepo

    def matricularEstudante(self, estudante: Estudante):
        try:
            self.estudantesRepo.get_by_matricula(estudante.matricula)
            raise ValueError("Matricula de aluno já existente")
        except RuntimeError:
            self.estudantesRepo.create(estudante)

    def cadastrarProfessor(self, professor: Professor):
        try:
            self.professoresRepo.get_by_matricula(professor.matricula)
            raise ValueError("Cadastro de professor já existente para a matrícula informada")
        except RuntimeError:
            self.professoresRepo.create(professor)

    def cadastrarTae(self, tae: TecnicoAdministrativo):
        try:
            self.taesRepo.get_by_matricula(tae.matricula)
            raise ValueError("Cadastro de TAE já existente para a matrícula informada")
        except RuntimeError:
            self.taesRepo.create(tae)
