from abc import abstractmethod

from domain.entity.TecnicoAdministrativo import TecnicoAdministrativo
from domain.entity.Utils import Departamento, Setor, Perfil
from domain.repository.IPessoaRepository import IPessoaRepository


class ITecnicoAdministrativoRepository(IPessoaRepository):

    @abstractmethod
    def find_all(self) -> [TecnicoAdministrativo]:
        pass

    @abstractmethod
    def find_nome_contem(self, nome: str) -> [TecnicoAdministrativo]:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> TecnicoAdministrativo:
        pass

    @abstractmethod
    def get_by_matricula(self, email: str) -> TecnicoAdministrativo:
        pass

    @abstractmethod
    def find_taes_setor_departamento(self, setor: Setor, departamento: Departamento) -> TecnicoAdministrativo:
        pass

    def perfil(self) -> Perfil:
        return Perfil.TAE
