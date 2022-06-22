# Importação para usar na Classe Pai
from abc import ABC


# Listas para a Classe Aluno
nome_aluno = list()
idade_aluno = list()
cpf_aluno = list()
mat_aluno = list()
curso_aluno = list()

#Listas para a Classe Funcionario
nome_func = list()
idade_func = list()
cpf_func = list()
cargo_func = list()

#Lista para a Classe Curso
nome_curso = list()
sem_curso = list()
mod_curso = list()


# Classe Pai
class Pessoa(ABC):

    # Método Construtor
    def __init__(self, nome, idade, cpf):
        self.__nome = nome
        self.__idade = idade
        self.__cpf = cpf


# Classe Filha
class Aluno(Pessoa):

    # Método Construtor
    def __init__(self, nome, idade, cpf, matricula, curso):
        super().__init__(nome, idade, cpf)
        self.__matricula = matricula
        self.__curso = curso

    # Método para Cadastrar propriedades em suas listar
    def cadastrar_aluno(self):

        nome = self._Pessoa__nome
        nome_aluno.append(nome)

        idade = self._Pessoa__idade
        idade_aluno.append(idade)

        cpf = self._Pessoa__cpf
        cpf_aluno.append(cpf)

        matricula = self.__matricula
        mat_aluno.append(matricula)

        curso = self.__curso
        curso_aluno.append(curso)
    
    # Método para Listar
    def listar_alunos(self):
        for i in range(len(nome_aluno)):
            print('-'*30)
            print(f" Aluno: {nome_aluno[i]}\n Idade: {idade_aluno[i]}\n CPF: {cpf_aluno[i]}\n Matrícula: {mat_aluno[i]}\n Curso: {curso_aluno[i]}")


# Classe Filha
class Funcionario(Pessoa):

    # Método Construtor
    def __init__(self, nome, idade, cpf, cargo):
        super().__init__(nome, idade, cpf)
        self.__cargo = cargo
    
    # Método para Cadastrar propriedades em suas listar
    def cadastrar_func(self):

        nome = self._Pessoa__nome
        nome_func.append(nome)

        idade = self._Pessoa__idade
        idade_func.append(idade)

        cpf = self._Pessoa__cpf
        cpf_func.append(cpf)

        cargo = self.__cargo
        cargo_func.append(cargo)
    
    # Método para Listar
    def listar_funcionarios(self):
        for i in range(len(nome_func)):
            print('-'*30)
            print(f" Funcionário: {nome_func[i]}\n Idade: {idade_func[i]}\n CPF: {cpf_func[i]}\n Cargo: {cargo_func[i]}")


class Curso():

    # Método Construtor
    def __init__(self, nome, semestres, modalidade):
        self.__nome = nome
        self.__semestres = semestres
        self.__modalidade = modalidade
    
    # Método para Cadastrar propriedades em suas listar
    def cadastrar_curso(self):

        nome = self.__nome
        nome_curso.append(nome)

        semestre = self.__semestres
        sem_curso.append(semestre)

        modalidade = self.__modalidade
        mod_curso.append(modalidade)

    # Método para Listar
    def listar_cursos(self):
        for i in range(len(nome_curso)):
            print('-'*30)
            print(f" Curso: {nome_curso[i]}\n Semestres: {sem_curso[i]}\n Modalidade: {mod_curso[i]}")