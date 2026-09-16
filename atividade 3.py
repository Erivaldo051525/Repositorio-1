produto = str(input("Digite seu nome do produto: "))  # Controle de estoque de equipamentos atividade 3
quantidade = int(input("Digite a quantidade existente do produto = "))

if quantidade == 0:
    estoque = "produto esgotado"
    

elif quantidade <=5:
    estoque= "Estoque critico"

elif quantidade <= 20: 
    estoque= "Estoque baixo"

elif quantidade >21:
    estoque= "Estoque normal"

else: quantidade= "nao cadastrado"
    

print("=== Estoque do produto ---")
print ("produto: ", produto)
print ("quantidade disponivel: ", quantidade)
print ("estoque: ", estoque)




