from datetime import datetime

from domain.entity.Estudante import Estudante
from domain.entity.Professor import Professor
from domain.entity.TecnicoAdministrativo import TecnicoAdministrativo
from domain.entity.Utils import Departamento, Setor

MEMORY_MATRICULAS = [

    # DISCENTES
    Estudante(
        nome="Samantha Muller",
        matricula="1234567",
        email="samanthaspurs@gmail.com",
        cpf="013.244.290-62",
        dataNascimento=datetime(day=12, month=4, year=1988),
        curso="História"
    ),
    Estudante(
        nome="Lennon da Silva Rocha",
        matricula="2040805",
        email="lennon.silva95@gmail.com",
        cpf="861.383.750-68",
        dataNascimento=datetime(day=14, month=11, year=1995),
        curso="História"
    ),
    Estudante(
        nome="Fulano de Tal",
        matricula="1030509",
        email="fulanodetal@gmail.com",
        cpf="012.345.678---",
        dataNascimento=datetime(day=11, month=11, year=1900),
        curso="História"
    ),

    # DOCENTES
    Professor(
        nome="Professor 1",
        matricula="0238461",
        email="professorum@gmail.com",
        cpf="013.244.19-11",
        dataNascimento=datetime(day=11, month=1, year=1960),
        departamento=Departamento.CCE
    ),
    Professor(
        nome="Outro Professor",
        matricula="2043505",
        email="outroprof@gmail.com",
        cpf="011.386.666-61",
        dataNascimento=datetime(day=16, month=4, year=1975),
        departamento=Departamento.CFH
    ),
    Professor(
        nome="Doutor Estranho",
        matricula="5030531",
        email="estranhodoutor@gmail.com",
        cpf="012.345.678-99",
        dataNascimento=datetime(day=11, month=11, year=1900),
        departamento=Departamento.CCJ
    ),

    # TAES
    TecnicoAdministrativo(
        nome="Funcionario 1",
        matricula="0238461",
        email="esteehumfunc@gmail.com",
        cpf="555.111.777-57",
        dataNascimento=datetime(day=11, month=1, year=1960),
        departamento=Departamento.CCE,
        setor=Setor.DP
    ),
    TecnicoAdministrativo(
        nome="Segundo Funcionario",
        matricula="1928367",
        email="maisumfunc@gmail.com",
        cpf="151.886.511-62",
        dataNascimento=datetime(day=16, month=4, year=1975),
        departamento=Departamento.CFH,
        setor=Setor.ADMINISTRATIVO
    ),
    TecnicoAdministrativo(
        nome="Outro Funcionario",
        matricula="1111444",
        email="umoutrofuncgmail.com",
        cpf="011.111.222-77",
        dataNascimento=datetime(day=11, month=11, year=1900),
        departamento=Departamento.CCJ,
        setor=Setor.FINANCEIRO
    ),
]
