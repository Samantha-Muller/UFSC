from domain.entity.TecnicoAdministrativo import TecnicoAdministrativo
from domain.entity.Utils import Departamento, Setor
from domain.repository.ITecnicoAdministrativoRepository import ITecnicoAdministrativoRepository
from infrastructure.persistence.InMemoryPessoaRepository import InMemoryPessoaRepository


class InMemoryTecnicoAdministrativoRepository(InMemoryPessoaRepository, ITecnicoAdministrativoRepository):

    def find_taes_setor_departamento(self, setor: Setor, departamento: Departamento) -> [TecnicoAdministrativo]:
        taes = self.find_all()
        taes = list(filter(lambda x: x.get_departamento() == departamento, taes))
        taes = list(filter(lambda x: x.get_setor() == setor, taes))
        return taes
