from faculdade import Faculdade

while True:

    # Menu Inicial
    print("-"*30)
    print("""Sistema Acadêmico:
    [ 1 ] Cadastrar Aluno
    [ 2 ] Listar Alunos
    [ 3 ] Sair""")
    opcao = int(input("Digita sua opção: "))
    print("-"*30)


    # Opção 1: Cadastrar Aluno
    if opcao == 1:
        faculdade = Faculdade()

        # Adicionando o Nome do Aluno
        nome = str(input("Digite o Nome do Aluno: "))
        faculdade.inserirAluno(nome)

        # Adicionando a Matrícula do Aluno
        matricula = int(input("Digite a Matrícula do Aluno: "))
        faculdade.inserirMatricula(matricula)

        # Adicionando o Nome do Curso do Aluno
        curso = str(input("Digite o Nome do Curso: "))
        faculdade.inserirCursos(curso)

        # Adicionando a Modalidade do Curso
        modalidade = str(input("Digite a Modalidade do Curso: "))
        faculdade.inserirModalidade(modalidade)

        # Testando...
        print(len(faculdade.matricula))
    

    # Opção 2: Listar Alunos
    elif opcao == 2:
        print("Listar Alunos em Desenvolvimento...")
    

    # Opção 3: Sair
    elif opcao == 3:
        print("Saindo do Sistema...")
        break

