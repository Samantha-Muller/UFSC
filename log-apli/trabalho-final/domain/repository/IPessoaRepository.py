from abc import ABC, abstractmethod

from domain.entity.Pessoa import Pessoa
from domain.entity.Utils import Perfil


class IPessoaRepository(ABC):

    @abstractmethod
    def create(self, pessoa: Pessoa):
        pass

    @abstractmethod
    def update(self, pessoa: Pessoa, matricula: str):
        pass

    @abstractmethod
    def delete(self, matricula: str):
        pass

    @abstractmethod
    def find_all(self) -> [Pessoa]:
        pass

    @abstractmethod
    def find_nome_contem(self, nome: str) -> [Pessoa]:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> Pessoa:
        pass

    @abstractmethod
    def get_by_matricula(self, email: str) -> Pessoa:
        pass

    @abstractmethod
    def perfil(self) -> Perfil:
        pass
