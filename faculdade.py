# from readline import append_history_file

class Faculdade:
    def __init__(self):
        self.aluno = list()
        self.matricula = list()
        self.curso = list()
        self.modalidade = list()
        self.estagio = list()

    def inserirAluno(self, aluno):
        self.aluno.append(aluno)

    def inserirMatricula(self, matricula):
        self.matricula.append(matricula)

    def inserirCursos(self, curso):
        self.curso.append(curso)

    def inserirModalidade(self, modalidade):
        self.modalidade.append(modalidade)

    def imprimir(self):
        print(f'Aluno {self.aluno} da matricula {self.matricula} do curso {self.curso} esta na modalidade {self.modalidade} status Cursando ')

    def InserirEstagio(self,estagio):
        self.estagio.append(estagio)    