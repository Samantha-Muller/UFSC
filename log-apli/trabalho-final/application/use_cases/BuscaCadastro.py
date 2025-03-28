from domain.entity.Estudante import Estudante
from domain.entity.Utils import Departamento, Setor
from domain.repository.IEstudanteRepository import IEstudanteRepository
from domain.repository.IProfessorRepository import IProfessorRepository
from domain.repository.ITecnicoAdministrativoRepository import ITecnicoAdministrativoRepository


class BuscaCadastro:
    def __init__(self,
                 estudantesRepo: IEstudanteRepository,
                 professoresRepo: IProfessorRepository,
                 taesRepo: ITecnicoAdministrativoRepository,
                 ):
        self.estudantesRepo = estudantesRepo
        self.professoresRepo = professoresRepo
        self.taesRepo = taesRepo

    def listarAlunosCurso(self, curso: str) -> [Estudante]:
        return self.estudantesRepo.find_estudantes_curso(curso)

    def listarProfessoresDepartamento(self, departamento: Departamento):
        return self.professoresRepo.find_professores_departamento(departamento)

    def listarTaesSetorDepartamento(self, departamento: Departamento, setor: Setor):
        return self.taesRepo.find_taes_setor_departamento(setor, departamento)

