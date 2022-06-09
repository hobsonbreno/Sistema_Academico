class Cursos:
    def __init__(self, nomec, idade, statusc=False, matricula=False):
        self.nomec = nomec
        self.idade = idade
        self.statusc = statusc 
        self.matricula = matricula
    
    def cursando (self,Nacionalidade,Estado_Civil,Profissão,CPF,Endereço,bairro,cep, curso , local,cadeira , professor):
        print(f'{self.nomec},{Nacionalidade},{Estado_Civil},{Profissão},inscrito no CPF sob o nº:{CPF},\nResidente e domiciliado na:{Endereço},no bairro:{bairro},CEP:{cep},\nEstá cursando {curso} na {local},\nAtualmente está concluindo a cadeira de {cadeira} com o professor {professor}.')
        self.status = True
