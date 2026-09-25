livros = []

while True:

    print("\n===== BIBLIOTECA =====")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Pesquisar livro")
    print("4 - Excluir livro")
    print("5 - Sair")
    print("6 - Quantidade desse exemplar")

    opcao = input("Digite uma opção: ")

    if opcao == "1":

        titulo = input("Digite o título: ")
        autor = input("Digite o autor: ")
        quantidade = int(input("Digite a quantidade:2 "))

        livros.append([titulo, autor, quantidade])

        print("Livro cadastrado!")

    elif opcao == "2":

        print("\n--- LIVROS CADASTRADOS ---")

        for contador in livros:
            print("Título:", contador[0])
            print("Autor:", contador[1])
            print("Quantidade:", contador[2])

    elif opcao == "3":

        pesquisa = input("Digite o título que deseja pesquisar: ")

        for contador in livros:
            if contador[0] == pesquisa:
                print("Livro encontrado!")
                print("Título:", contador[0])
                print("Autor:", contador[1])
                print("Quantidade:", contador[2])
                

    elif opcao == "4":

        pesquisa = input("Digite o título que deseja excluir: ")

        
        if contador[0] == pesquisa:
            livros.remove(contador)
            print("Livro excluído!")

    9   
    elif opcao == "5":

        print("Programa encerrado.")
        break
    
    
    else:

        print("Opção inválida!")