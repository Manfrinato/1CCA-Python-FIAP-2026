from email.policy import default

from disciplina import Disciplina


class Aluno:
    def __init__(self, nome, rm, curso):
        self.nome = nome
        self.rm = rm
        self.curso = curso
        self.disciplinas = []
        self.notas_por_disciplinas = {}

    def matricular(self,disciplina:Disciplina):
        self.disciplinas.append(disciplina)
        self.notas_por_disciplinas.setdefault(disciplina.nome)

    def adcionar_nota(self,disciplina, nota: float):
        self.notas_por_disciplinas [disciplina.nome].append(nota)

    def calcular_media_d(self,d: Disciplina)->float:
        notas = self.notas_por_disciplinas.get(d.nome, [])
        return sum(notas) / len(notas)
