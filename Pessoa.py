class Pessoa:
    def _init_(self, nome,telefone , cpf, matricula, email):
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf
        self.matricula = matricula
        self.email = email


class Funcionario(Pessoa):
    def _init_(self, matricula, cargo, salario,status):
        self.__matricula = matricula
        self._cargo = cargo
        self._salario = salario
        self.status = status

class Aluno(Pessoa):
    def _init_(self, profissao, renda, status):
        self.profissao = profissao
        self.renda = renda
        self.status = status


