<<<<<<< HEAD


class Faculdade():
    
    def inserirAluno(self, aluno):
        estudante = aluno
        alunos.append(estudante)

    def inserirMatricula(self, matricula):
        estudante = matricula
        matriculas.append(estudante)

    def inserirCurso(self, curso):
        estudante = curso
        cursos.append(estudante)

    def inserirModalidade(self, modalidade):
        estudante = modalidade
        modalidades.append(estudante)

    def inserirCargos(self, cargo):
        estudante = cargo
        cargos.append(estudante)

    def imprimir(self):
        print("alunos:", alunos, "matriculas: ", matriculas, "cursos: ",
              cursos, "modalidades: ", modalidades, "cargos: ", cargos)


alunos = []
matriculas = []
cursos = []
modalidades = []
cargos = []


class Pessoa(Faculdade):
    def __init__(self,nome,data_nascimento,cpf):
       self.nome = nome 
       self.data_nascimento = data_nascimento
       self.cpf = cpf 


class Aluno(Pessoa,Faculdade):
    def __init__(self,matricula,curso,modalidade):
       self.matricula = matricula
       self.curso = curso
       self.modalidade = modalidade


    def logarAluno(self, aluno):   

        if aluno not in self.alunos:
            print(f'Nome ou matricula incorretos ! {self.alunos}')
        else:
            print(f'Acesso liberado !')

    def imprimirAluno():
        print('lista de aluno',alunos)


class Funcionario(Pessoa,Faculdade):
     def __init__(self,cargo):
        self.cargos = cargo 





    
=======
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
>>>>>>> refs/remotes/origin/main
