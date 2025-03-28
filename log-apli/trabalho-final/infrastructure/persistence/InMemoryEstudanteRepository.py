from domain.entity.Estudante import Estudante
from infrastructure.persistence.InMemoryPessoaRepository import InMemoryPessoaRepository
from domain.repository.IEstudanteRepository import IEstudanteRepository


class InMemoryEstudanteRepository(InMemoryPessoaRepository, IEstudanteRepository):

    def find_estudantes_curso(self, curso: str) -> [Estudante]:
        estudantes = self.find_all()
        estudantes = list(filter(lambda x: x.get_curso() == curso, estudantes))
        return estudantes
