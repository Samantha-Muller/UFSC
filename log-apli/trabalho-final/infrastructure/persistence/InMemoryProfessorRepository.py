from domain.entity.Professor import Professor
from domain.entity.Utils import Departamento
from domain.repository.IProfessorRepository import IProfessorRepository
from infrastructure.persistence.InMemoryPessoaRepository import InMemoryPessoaRepository


class InMemoryProfessorRepository(InMemoryPessoaRepository, IProfessorRepository):

    def find_professores_departamento(self, departamento: Departamento) -> [Professor]:
        professores = self.find_all()
        professores = list(filter(lambda x: x.get_departamento() == departamento, professores))
        return professores
