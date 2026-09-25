print("SISTEMA PARA BIBLIOTECA")

print("1 - Cadrasto de Livros ")
print("2 - Cadastrar Alunos ")
print("3 - Realizar Emprestimo ")
print("4 - Sair") 

opcao = int(input("Escolha e digite a opção desejada = " ))

biblioteca = []

while True:
    print("\n=== Secao livros ===")
    print("1 - Cadastrar Livro")
    print("2 - Listar Livros")
    print("3 - Pesquisar Livro")
    print("4 - Alterar Livro")
    print("5 - Excluir Livro")
    print("6 - Quantidade de  Livros Cadastrados")
    print("7 - Sair")

    selecione = int(input("Escolha uma opção: "))

    if selecione == 1:
        codigo = int(input("Código do Livro: "))

    existe = False
    for livro in biblioteca:
            if livro["codigo"] == codigo:
                print("Erro: Já existe um livro cadastrado com este código.")
                existe = True
                break
            
    else:
            #codigo = input("Digite o codigo do Livro: ")
            titulo = input("Título do Livro: ")
            autor = input("Autor do Livro: ")
            ano = input("Ano do Livro:")
            estoque = input("Estoque:")
            
            livro = {"codigo": codigo, "titulo": titulo, "autor": autor, "ano" : ano, "estoque" : estoque}
                
             
            biblioteca.append(livro)
            print("Livro cadastrado com sucesso!")


    if selecione == 2:
        if not biblioteca:
            print("Nenhum livro cadastrado.")
        else:
            print("\n--- LISTA DE LIVROS ---")
            for livro in biblioteca:
                print(f"Código: {livro['codigo']} | Título: {livro['titulo']} | Autor: {livro['autor']}")

    if selecione == 3:
        codigo = int(input("Digite o código do livro que deseja buscar: "))
        encontrado = False
        for livro in biblioteca:
            if livro["codigo"] == codigo:
                print(f"Encontrado -> Código: {livro['codigo']} | Título: {livro['titulo']} | Autor: {livro['autor']}")
                encontrado = True
                break
        if not encontrado:
            print("Livro não encontrado.")

    if selecione == "4":
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

    if selecione == "5":
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

    if selecione == "6":
        print(len(biblioteca))
        break
              

    if selecione == "7":
        print("Saindo do sistema... Até logo!")

#else:
 #       print("Opção inválida! Tente novamente.")



