biblioteca = []

while True:
    print("\n=== Secao livros ===")
    print("1 - Cadastrar Livro")
    print("2 - Listar Livros")
    print("3 - Pesquisar Livro")
    print("4 - Alterar Livro")
    print("5 - Excluir Livro")
    print("6 - Quantidade de Livros Cadastrados")
    print("7 - Sair")

    try:
        selecione = int(input("Escolha uma opção: "))
    except ValueError:
        print("Erro: Digite apenas números válidos.")
        continue

    # 1 - CADASTRAR LIVRO
    if selecione == 1:
        try:
            codigo = int(input("Código do Livro: "))
            
            # Verifica se já existe um livro com o código informado
            existe = False
            for livro in biblioteca:
                if livro["codigo"] == codigo:
                    print("Erro: Já existe um livro cadastrado com este código.")
                    existe = True
                    break

            # Só cadastra se o código não existir na lista
            if not existe:
                titulo = input("Título do Livro: ").strip()
                autor = input("Autor do Livro: ").strip()
                ano = input("Ano do Livro: ").strip()
                estoque = input("Estoque: ").strip()

                livro = {
                    "codigo": codigo, 
                    "titulo": titulo, 
                    "autor": autor, 
                    "ano": ano, 
                    "estoque": estoque
                }

                biblioteca.append(livro)
                print("Livro cadastrado com sucesso!")
        except ValueError:
            print("Erro: O código deve ser um número inteiro.")

    # 2 - LISTAR LIVROS
    elif selecione == 2:
        if not biblioteca:
            print("Nenhum livro cadastrado.")
        else:
            print("\n--- LISTA DE LIVROS ---")
            for livro in biblioteca:
                print(f"Código: {livro['codigo']} | Título: {livro['titulo']} | Autor: {livro['autor']} | Ano: {livro['ano']} | Estoque: {livro['estoque']}")

    # 3 - PESQUISAR LIVRO
    elif selecione == 3:
        try:
            codigo = int(input("Digite o código do livro que deseja buscar: "))
            encontrado = False
            for livro in biblioteca:
                if livro["codigo"] == codigo:
                    print(f"Encontrado -> Código: {livro['codigo']} | Título: {livro['titulo']} | Autor: {livro['autor']}")
                    encontrado = True
                    break
            if not encontrado:
                print("Livro não encontrado.")
        except ValueError:
            print("Erro: Digite um código numérico válido.")

    # 4 - ALTERAR LIVRO
    elif selecione == 4:
        try:
            codigo = int(input("Digite o código do livro a alterar: "))
            encontrado = False
            for livro in biblioteca:
                if livro["codigo"] == codigo:
                    livro["titulo"] = input("Novo Título: ").strip()
                    livro["autor"] = input("Novo Autor: ").strip()
                    livro["ano"] = input("Novo Ano: ").strip()
                    livro["estoque"] = input("Novo Estoque: ").strip()
                    print("Livro alterado com sucesso!")
                    encontrado = True
                    break
            if not encontrado:
                print("Livro não encontrado.")
        except ValueError:
            print("Erro: Digite um código numérico válido.")

    # 5 - EXCLUIR LIVRO
    elif selecione == 5:
        try:
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
        except ValueError:
            print("Erro: Digite um código numérico válido.")

    # 6 - QUANTIDADE DE LIVROS CADASTRADOS
    elif selecione == 6:
        print(f"\nTotal de livros cadastrados: {len(biblioteca)}")

    # 7 - SAIR
    elif selecione == 7:
        print("Saindo do sistema... Até logo!")
        break

    else:
        print("Opção inválida. Escolha um número de 1 a 7.")



    elif selecione == 3:
        try:
            codigo = int(input("Digite o código do livro que deseja buscar: "))
            encontrado = False
            for livro in biblioteca:
                if livro["codigo"] == codigo:
                    print(f"Encontrado -> Código: {livro['codigo']} | Título: {livro['titulo']} | Autor: {livro['autor']}")
                    encontrado = True
                    break
            if not encontrado:
                print("Livro não encontrado.")
        except ValueError:
            print("Erro: Digite um código numérico válido.")