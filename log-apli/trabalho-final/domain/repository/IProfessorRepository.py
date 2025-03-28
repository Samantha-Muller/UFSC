from abc import abstractmethod

from domain.entity.Professor import Professor
from domain.entity.Utils import Departamento, Perfil
from domain.repository.IPessoaRepository import IPessoaRepository


class IProfessorRepository(IPessoaRepository):

    @abstractmethod
    def find_all(self) -> [Professor]:
        pass

    @abstractmethod
    def find_nome_contem(self, nome: str) -> [Professor]:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> Professor:
        pass

    @abstractmethod
    def get_by_matricula(self, email: str) -> Professor:
        pass

    @abstractmethod
    def find_professores_departamento(self, departamento: Departamento) -> [Professor]:
        pass

    def perfil(self) -> Perfil:
        return Perfil.PROFESSOR
