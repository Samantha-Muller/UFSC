from abc import ABC

from domain.entity.Pessoa import Pessoa
from domain.repository.IPessoaRepository import IPessoaRepository
from infrastructure.persistence.dao.InMemoryDao import MEMORY_MATRICULAS


class InMemoryPessoaRepository(IPessoaRepository, ABC):

    def create(self, pessoa: Pessoa):
        MEMORY_MATRICULAS.append(pessoa)

    def update(self, pessoa: Pessoa, matricula: str):
        self.delete(matricula)
        self.create(pessoa)

    def delete(self, matricula: str):
        pessoas = list(filter(lambda x: x.get_matricula() != matricula, MEMORY_MATRICULAS))
        MEMORY_MATRICULAS.clear()
        MEMORY_MATRICULAS.extend(pessoas)

    def find_all(self) -> [Pessoa]:
        pessoas = list(filter(lambda x: x.get_perfil() == self.perfil(), MEMORY_MATRICULAS))
        return pessoas

    def find_nome_contem(self, nome: str) -> [Pessoa]:
        pessoas = self.find_all()
        pessoas = list(filter(lambda x: nome in x.get_nome(), pessoas))
        return pessoas

    def get_by_email(self, email: str) -> Pessoa:
        pessoas = self.find_all()
        pessoas = list(filter(lambda x: x.get_email() == email, pessoas))
        if not pessoas:
            raise RuntimeError(f"Nenhum estudante cadastrado para o e-mail {email}")
        return pessoas[0]

    def get_by_matricula(self, matricula: str) -> Pessoa:
        pessoas = self.find_all()
        pessoas = list(filter(lambda x: x.get_matricula() == matricula, pessoas))
        if not pessoas:
            raise RuntimeError(f"Matricula {matricula} não encontrada")
        return pessoas[0]
