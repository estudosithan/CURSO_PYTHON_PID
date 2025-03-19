class Curso:
    def __init__(self, nome):
        self.nome = nome

class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.cursos = []  # Lista de cursos

    def adicionar_curso(self, curso):
        self.cursos.append(curso)  # Agregação

curso1 = Curso("Python")
curso2 = Curso("JavaScript")
aluno = Aluno("João")
aluno.adicionar_curso(curso1)
aluno.adicionar_curso(curso2)