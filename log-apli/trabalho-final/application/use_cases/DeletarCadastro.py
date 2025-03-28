from domain.entity.Utils import Perfil
from domain.repository.IEstudanteRepository import IEstudanteRepository
from domain.repository.IProfessorRepository import IProfessorRepository
from domain.repository.ITecnicoAdministrativoRepository import ITecnicoAdministrativoRepository


class DeletarCadastro:
    def __init__(self,
                 estudantesRepo: IEstudanteRepository,
                 professoresRepo: IProfessorRepository,
                 taesRepo: ITecnicoAdministrativoRepository,
                 ):
        self.estudantesRepo = estudantesRepo
        self.professoresRepo = professoresRepo
        self.taesRepo = taesRepo

    def deletar(self, perfil: Perfil, matricula: str):
        if perfil == Perfil.ESTUDANTE:
            self.estudantesRepo.delete(matricula)
        elif perfil == Perfil.PROFESSOR:
            self.professoresRepo.delete(matricula)
        else:
            self.taesRepo.delete(matricula)
