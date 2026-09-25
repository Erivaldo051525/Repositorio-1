


biblioteca = []

while True:
    print("\n=== SISTEMA DE BIBLIOTECA ===")
    print("1 - Cadastrar Livro")
    print("2 - Listar Livros")
    print("3 - Pesquisar Livro")
    print("4 - Alterar Livro")
    print("5 - Excluir Livro")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        codigo = int(input("Código do Livro: "))

        existe = False
        for livro in biblioteca:
            if livro["codigo"] == codigo:
                existe = True
                break

        if existe:
            print("Erro: Já existe um livro cadastrado com este código.")
        else:
            titulo = input("Título do Livro: ")
            autor = input("Autor do Livro: ")
            
            livro = {
                "codigo": codigo,
                "titulo": titulo,
                "autor": autor
            }
            biblioteca.append(livro)
            print("Livro cadastrado com sucesso!")


    elif opcao == "2":
        if not biblioteca:
            print("Nenhum livro cadastrado.")
        else:
            print("\n--- LISTA DE LIVROS ---")
            for livro in biblioteca:
                print(f"Código: {livro['codigo']} | Título: {livro['titulo']} | Autor: {livro['autor']}")

    elif opcao == "3":
        codigo = int(input("Digite o código do livro que deseja buscar: "))
        encontrado = False
        for livro in biblioteca:
            if livro["codigo"] == codigo:
                print(f"Encontrado -> Código: {livro['codigo']} | Título: {livro['titulo']} | Autor: {livro['autor']}")
                encontrado = True
                break
        if not encontrado:
            print("Livro não encontrado.")

    elif opcao == "4":
        codigo = int(input("Digite o código do livro a alterar: "))
        encontrado = False
        for livro in biblioteca:
            if livro["codigo"] == codigo:
                livro["titulo"] = input("Novo Título: ")
                livro["autor"] = input("Novo Autor: ")
                print("Livro alterado com sucesso!")
                encontrado = True
                break
        if not encontrado:
            print("Livro não encontrado.")

    elif opcao == "5":
        codigo = int(input("Digite o código do livro a excluir: "))
        encontrado = False
        for i, livro in enumerate(biblioteca):
            if livro["codigo"] == codigo:
                del biblioteca[i]
                print("Livro excluído com sucesso!")
                encontrado = True
                break
        if not encontrado:
            print("Livro não encontrado.")

    elif opcao == "6":
        print("Saindo do sistema... Até logo!")
        break

    else:
        print("Opção inválida! Tente novamente.")