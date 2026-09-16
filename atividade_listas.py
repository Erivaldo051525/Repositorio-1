#Lista  Posições e acesso aos elementos    Alterando uma lista
nomes = ["Ana", "Carlos", "João", "Maria"]
print(nomes[0])
print(nomes[1])
print(nomes[2])
print(nomes[3])
print(nomes[-1])

print(len(nomes)) #comando para saber o tamanho da lista neste caso quantos nomes tem a lista sempre comecando do 0 - se o tam desta e 4
print()
nomes[1]= "Pedro" # esse comendo permite substituir o nome da posicao 1 (Carlos) por Pedro 
print(nomes) #lista alterada
print()

nomes.insert(1, "Lucas") #Para inserir em uma posição específica, usamos insert().
print(nomes)
print()
nomes.remove("Maria")  #comando remove(), quando conhecemos o valor, remove um valor neste caso sao os valares sao nomes
print(nomes)
print()
nomes.pop(1) #comando pop(), quando conhecemos a posição, remove um valor usando sua posição.
print(nomes)
print()
