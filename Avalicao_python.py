print("SISTEMA PARA BIBLIOTECA")
print()
print("1 - Cadastrar Livros ")
print()
print("2 - Cadastrar Alunos ")
print()
print("3 - Realizar Emprestimo ")
print()
print("4 - Sair") 
print() 

opcao = int(input("Escolha e digite a opção desejada = " ))

if opcao ==1:
    quantidade= int(input("Quantos livros quer cadastrar = "))
    for i in range(quantidade):
        print(f"----- LIVRO {i + 1} -----")

        codigo =str(input("Codigo do livro: ")) 
        titulo =str(input("Titulo do livro: "))
        autor =str(input("Nome do autor: "))
        ano = int(input("Ano da publicação: "))
        if len(str(ano))==4: 
            print("Ano válido!")
        else:
            print("O ano deve conter 4 digitos numericos")

        estoque = int(input("Quantidade disponivel="))
        print()
        print("Parabens, Livro Cadrastado com sucesso")

elif opcao ==2:
    quantidade= int(input("Quantos alunos quer cadastrar = "))
    for i in range(quantidade):
        print(f"----- ALUNO {i + 1} -----")
        matricula =int(input("Matricula do Aluno: "))
        nome =str(input("Nomo do Aluno: "))
        serie_turma =str(input("Serie e turma do aluno: "))
        
        print("Aluno cadastrado com sucesso")

elif opcao ==3:
        
        codigo =int(input("Codigo do Livro: "))
        matricula =int(input("Informe a matricula do aluno: "))
        estoque =int(input("Quantidade disponivel: ",))    #quero mostrar a quantidade de livro disponiveis feitas no cadastro de livros   
        print("Livro emprestdo com sucesso")

        if estoque ==0:
             print("Não ha exemplares disponiveis, protanto não sera possivel realizar o emprestimo")

        else: 
            
            print("Informações do seu emprestimo")
            print("Codigo do Livro:", codigo)
            print(f"Matricula do Aluno:, {matricula}")
            print("Emprestimo realizado com sucesso")

elif opcao ==4:
     print("Sair do sistema")

else: 
    
    print("Opção Inválida, Escolha uma opções válidas: 1, 2, 3 ou 4.")

       