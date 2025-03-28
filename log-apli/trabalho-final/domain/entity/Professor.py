from datetime import datetime

from domain.entity.Pessoa import Pessoa
from domain.entity.Utils import Departamento, Perfil


class Professor(Pessoa):

    def __init__(
            self,
            nome: str,
            matricula: str,
            email: str,
            cpf: str,
            dataNascimento: datetime,
            departamento: Departamento
    ):
        super().__init__(nome, matricula, email, cpf, dataNascimento)
        self.departamento = departamento

    def set_departamento(self, departamento: Departamento):
        self.departamento = departamento

    def get_departamento(self) -> Departamento:
        return self.departamento

    def get_perfil(self) -> Perfil:
        return Perfil.PROFESSOR
