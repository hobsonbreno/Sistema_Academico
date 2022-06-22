from faculdade import Faculdade

while True:

    # Menu Inicial
    print("="*30)
    print("""Sistema Acadêmico:
    [ 1 ] Cadastrar Aluno
    [ 2 ] Listar Alunos
    [ 3 ] Sair""")
    opcao = int(input("Digita sua opção: "))
    print("="*30)

    # Criação do Objeto
    x = Faculdade()

    # Opção 1: Cadastrar Dados do Aluno
    if opcao == 1:
        aluno = str(input("Digite o nome do aluno: "))
        x.inserirAluno(aluno)

        matricula = int(input("Digite o nome do matricula: "))
        x.inserirMatricula(matricula)

        curso = str(input("Digite o nome do curso: "))
        x.inserirCurso(curso)

        modalidade = str(input("Digite o nome do modalidade: "))
        x.inserirModalidade(modalidade)

        cargos = str(input("Digite o nome do cargos: "))
        x.inserirCargos(cargos)

    # Opção 2: Listar Dados dos Alunos
    elif opcao == 2:
        x.imprimir()

    # Opção 3: Sair do Sistema
    elif opcao == 3:
        print("Sistema encerrado!")
        break
