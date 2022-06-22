from faculdade import Aluno, Funcionario, Curso

while True:

    # Menu Inicial
    print("="*30)
    print("""Sistema Acadêmico:
    [ 1 ] Cadastrar Aluno
    [ 2 ] Cadastrar Funcionario
    [ 3 ] Cadastrar Curso
    [ 4 ] Listar Alunos
    [ 5 ] Listar Funcionario
    [ 6 ] Listar Curso
    [ 7 ] Sair""")
    opcao = int(input("Digita sua opção: "))
    print("="*30)

    # Opção 1: Cadastrar Dados do Aluno
    if opcao == 1:

        # Inputs para inserir os dados
        nome_aluno = str(input("Digite o Nome: "))
        idade_aluno = int(input("Digite a Idade: "))
        cpf_aluno = int(input("Digite o CPF: "))
        matricula_aluno = int(input("Digite a Matrícula: "))
        curso_aluno = str(input("Digite o Curso: "))

        # Cadastrando o Aluno, criando um objeto e usando o método 
        aluno = Aluno(nome_aluno, idade_aluno, cpf_aluno, matricula_aluno, curso_aluno)
        aluno.cadastrar_aluno()
    

    # Opção 2: Cadastrar Dados do Funcionarios
    if opcao == 2:
        
        # Inputs para inserir os dados
        nome_func = str(input("Digite o Nome: "))
        idade_func = int(input("Digite a Idade: "))
        cpf_func = int(input("Digite o CPF: "))
        cargo_func = str(input("Digite o Cargo: "))

        # Cadastrando o Funcionário, criando um objeto e usando o método
        func = Funcionario(nome_func, idade_func, cpf_func, cargo_func)
        func.cadastrar_func()


    # Opção 3: Cadastrar Dados do Cursos
    if opcao == 3:

        # Inputs para inserir os dados
        nome_curso = str(input("Digite o Nome: "))
        semestres_curso = int(input("Digite a quantidade de Semestres: "))
        modalidade_curso = str(input("Digite a Modalide do Curso: "))

        # Cadastrando o Curso, criando um objeto e usando o método
        curso = Curso(nome_curso, semestres_curso,modalidade_curso)
        curso.cadastrar_curso()


    # Opção 4: Listar Dados dos Alunos
    elif opcao == 4:
        aluno.listar_alunos()


    # Opção 5: Listar dados dos Funcionarios
    elif opcao == 5:
        func.listar_funcionarios()


    # Opção 6: Listar dados dos Cursos
    elif opcao == 6:
        curso.listar_cursos()


    # Opção 7: Sair do Sistema
    elif opcao == 7:
        print("Sistema encerrado!")
        break

