from enum import Enum


class Perfil(Enum):
    ESTUDANTE = "Estudante"
    PROFESSOR = "Professor"
    TAE = "Tecnico-Administrativo"


class Departamento(Enum):
    CCE = 1
    CFH = 2
    CSC = 3
    CFM = 4
    CED = 5
    CCJ = 6


class Setor(Enum):
    FINANCEIRO = 1
    ADMINISTRATIVO = 2
    DP = 3
