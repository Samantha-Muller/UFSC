from abc import abstractmethod

from domain.entity.Estudante import Estudante
from domain.entity.Utils import Perfil
from domain.repository.IPessoaRepository import IPessoaRepository


class IEstudanteRepository(IPessoaRepository):

    @abstractmethod
    def find_all(self) -> [Estudante]:
        pass

    @abstractmethod
    def find_nome_contem(self, nome: str) -> [Estudante]:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> Estudante:
        pass

    @abstractmethod
    def get_by_matricula(self, email: str) -> Estudante:
        pass

    @abstractmethod
    def find_estudantes_curso(self, curso: str) -> [Estudante]:
        pass

    def perfil(self) -> Perfil:
        return Perfil.ESTUDANTE
