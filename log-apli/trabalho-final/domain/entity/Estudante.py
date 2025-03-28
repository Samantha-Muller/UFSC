from datetime import datetime

from domain.entity.Pessoa import Pessoa
from domain.entity.Utils import Perfil


class Estudante(Pessoa):

    def __init__(
            self,
            nome: str,
            matricula: str,
            email: str,
            cpf: str,
            dataNascimento: datetime,
            curso: str
    ):
        super().__init__(nome, matricula, email, cpf, dataNascimento)
        self.curso = curso

    def get_curso(self) -> str:
        return self.curso

    def set_curso(self, curso: str):
        self.curso = curso

    def get_perfil(self) -> Perfil:
        return Perfil.ESTUDANTE
