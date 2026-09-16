#lista de produtos
produtos = ["Teclado", "Mouse", "Monitor", "Headset"]
for produto in produtos:  #Listando todos os produtos:
    print(produto)

produtos.append("Webcam") #Adicionando um novo produto:
print(produtos)

for produto in produtos:  #Listando todos os produtos:
    print(produto)

produtos[1] = "Mouse sem fio" #Alterando um produto pela posição:
print(produtos)

if "Monitore" in produtos:  #Procurando um produto:
    print("Produto encontrado!")
else:
    print("Produto não encontrado")

produtos.remove("Headset") #Removendo um produto:
print(produtos)