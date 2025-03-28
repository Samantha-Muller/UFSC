from application.use_cases import AtualizarCadastro
from application.use_cases.BuscaCadastro import BuscaCadastro
from application.use_cases.DeletarCadastro import DeletarCadastro
from application.use_cases.InserirCadastro import InserirCadastro


class MatriculaService:
    def __init__(self,
                 atualizarCadastro: AtualizarCadastro,
                 buscaCadastro: BuscaCadastro,
                 deletarCadastro: DeletarCadastro,
                 inserirCadastro: InserirCadastro,
                 ):
        self.atualizarCadastro = atualizarCadastro
        self.buscaCadastro = buscaCadastro
        self.deletarCadastro = deletarCadastro
        self.inserirCadastro = inserirCadastro
