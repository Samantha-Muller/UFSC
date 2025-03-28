from domain.entity.Utils import Departamento, Setor
from domain.repository.IEstudanteRepository import IEstudanteRepository
from domain.repository.IProfessorRepository import IProfessorRepository
from domain.repository.ITecnicoAdministrativoRepository import ITecnicoAdministrativoRepository


class AtualizarCadastro:
    def __init__(self,
                 estudantesRepo: IEstudanteRepository,
                 professoresRepo: IProfessorRepository,
                 taesRepo: ITecnicoAdministrativoRepository,
                 ):
        self.estudantesRepo = estudantesRepo
        self.professoresRepo = professoresRepo
        self.taesRepo = taesRepo

    def transferirAlunoDeCurso(self, matricula: str, novoCurso: str):
        estudante = self.estudantesRepo.get_by_matricula(matricula)
        estudante.set_curso(novoCurso)
        self.estudantesRepo.update(estudante, matricula)

    def transferirProfessorDeDepartamento(self, matricula: str, novoDepartamento: Departamento):
        prof = self.professoresRepo.get_by_matricula(matricula)
        prof.set_departamento(novoDepartamento)
        self.professoresRepo.update(prof, matricula)

    def transferirTaeDeSetor(self, matricula: str, novoSetor: Setor):
        tae = self.taesRepo.get_by_matricula(matricula)
        tae.set_setor(novoSetor)
        self.taesRepo.update(tae, matricula)
