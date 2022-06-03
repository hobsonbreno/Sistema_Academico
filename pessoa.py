class Pessoa:
    def __init__(self, nome, idade, status=False, matricula=False):
        self.nome = nome
        self.idade = idade
        self.status = status 
        self.matricula = matricula
    
    def cursando (self, curso , local, professor,matéria):
        print(f'{self.nome} está cursando {curso} na {local} e está na diciplina de {professor} com o professor {matéria}.')
        self.status = True
