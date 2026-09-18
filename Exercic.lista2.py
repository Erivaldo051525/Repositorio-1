#criando uma lista vazia com 6 valores
produtos=[]

#listado os produtos
for i in range(2):
     produto = input(f"produto {i+1} = ")
     produtos.append(produto) 

#listando os produtos cadrastrados
print("\n  Produtos Cadastradas:")

for contador in produtos:
    print(contador)

# mostrando a quantidade de prdotos cadastrados.
print(f" Quantidade de produtos cadastrados: {len(produtos)}")

#Procurando um produto

busca = input("\n Digite o procura que deseja pesquisar:")
print("Produto a ser encontrado:",busca)

if busca in produtos:
    print("produto Encontrado")
else:
    print("Produto Não encotrado")



    