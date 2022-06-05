class Pessoa:
    def __init__(self, nome, idade, status=False, matricula=False):
        self.nome = nome
        self.idade = idade
        self.status = status 
        self.matricula = matricula
    
    def cursando (self,Nacionalidade,Estado_Civil,Profissão,CPF,Endereço,bairro,cep, curso , local,cadeira , professor):
        print(f'{self.nome},{Nacionalidade},{Estado_Civil},{Profissão},inscrito no CPF sob o nº:{CPF},\nResidente e domiciliado na:{Endereço},no bairro:{bairro},CEP:{cep},\nEstá cursando {curso} na {local},\nAtualmente está concluindo a cadeira de {cadeira} com o professor {professor}.')
        self.status = True
