nomes = ["Ana", "Carlos", "João", "Erivaldo", "Oxto"]

print()
for nome in nomes:
    print(nomes)
print()


idades=[16, 17, 18, 20, 48, 60]
idade=1
for idade in idades:
    print(idades)

notas = [7, 8, 6, 9]
soma = 5
for nota in notas:
    soma = soma + nota
    print(soma)
    
print()    
notas = [20, 24, 35, 10]

for nota in notas:
    media = nota/4
    print(media)
print()
nomes = ["Carlos", "Ana", "João", "Erivaldo", "Oxto", "Erivaldo"]
#"Ana" in nomes  
posicao= nomes.index("Erivaldo") #Encontrar posição   Retorna o índice do valor.
print(posicao)

localizar= "Ana" in nomes  #Verificar se existe  Retorna True ou False.
print(localizar)

contar=nomes.count("Erivaldo") #Conta quantas vezes o valor aparece.
print(contar)

ordenar =nomes.sort() #ordena em ordam alfabetica
print(nomes)

notas = [8, 6, 9, 7]
ordenar = notas.sort() #ordena em ordam crescente
print(notas)

notas.sort(reverse=True) #ordena em ordam decrescente
print(notas)

nova=nomes.copy() #cria copia de uma lista
print(nova)

nome="Erivaldoo"
if nome in nomes:
    print("Nome encontrado")
else:
    print("Nome não encontrado")

