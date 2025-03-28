from abc import ABC, abstractmethod
from _datetime import datetime

from domain.entity.Utils import Perfil


class Pessoa(ABC):

    def __init__(
            self,
            nome: str,
            matricula: str,
            email: str,
            cpf: str,
            dataNascimento: datetime
    ):
        self.nome = nome
        self.matricula = matricula
        self.email = email
        self.cpf = cpf
        self.dataNascimento = dataNascimento

    def get_nome(self) -> str:
        return self.nome

    def set_nome(self, nome: str):
        self.nome = nome

    def get_matricula(self) -> str:
        return self.matricula

    def set_matricula(self, matricula: str):
        self.matricula = matricula

    def get_email(self) -> str:
        return self.email

    def set_email(self, email: str):
        self.email = email

    def get_cpf(self) -> str:
        return self.cpf

    def set_cpf(self, cpf: str):
        self.cpf = cpf

    def get_data_nascimento(self) -> str:
        return self.cpf

    def set_data_nascimento(self, dataNascimento: datetime):
        self.dataNascimento = dataNascimento

    @abstractmethod
    def get_perfil(self) -> Perfil:
        pass
