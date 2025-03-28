from datetime import datetime

from domain.entity.Pessoa import Pessoa
from domain.entity.Utils import Departamento, Setor, Perfil


class TecnicoAdministrativo(Pessoa):

    def __init__(
            self,
            nome: str,
            matricula: str,
            email: str,
            cpf: str,
            dataNascimento: datetime,
            departamento: Departamento,
            setor: Setor
    ):
        super().__init__(nome, matricula, email, cpf, dataNascimento)
        self.departamento = departamento
        self.setor = setor

    def set_departamento(self, departamento: Departamento):
        self.departamento = departamento

    def get_departamento(self) -> Departamento:
        return self.departamento

    def set_setor(self, setor: Setor):
        self.setor = setor

    def get_setor(self) -> Setor:
        return self.setor

    def get_perfil(self) -> Perfil:
        return Perfil.TAE
