

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
        for i in range(len(alunos)):
            print('-'*30)
            print(f"Alunos: {alunos[i]}\n matriculas: {matriculas[i]}\n cursos: {cursos[i]}\n modalidades: {modalidades[i]}\n cargos: {cargos[i]}")


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





    
