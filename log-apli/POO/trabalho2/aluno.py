class Aluno:
    def __init__(self, nome, curso, tempoSemDormir):
        self.nome = nome
        self.curso = curso
        self.tempoSemDormir = tempoSemDormir

    def estudar(self, horasEstudo):
        self.tempoSemDormir += horasEstudo

    def dormir(self, horasSono):
        self.tempoSemDormir -= horasSono
