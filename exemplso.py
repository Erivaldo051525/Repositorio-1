#Contando números com range() A função range(inicio, fim) gera uma sequência de números. Atenção: O Python para antes do número final. Para contar de 1 a 5, usamos range(1, 6):
print("Contando de 1 a 5:")
for numero in range(1, 6):
    print(numero)


#Percorrendo uma lista de alunos  - Este exemplo se encaixa perfeitamente no menu que você acabou de criar. O for pega um nome por vez de dentro da lista:
alunos = ["Ana", "Bruno", "Carlos", "Diana"]

print("Lista de Alunos Cadastrados:")
for aluno in alunos:
    print(f"🎓 Nome: {aluno}")

# Calculando a Tabuada (Matemática)Você pode usar a variável do for para fazer contas automaticamente a cada repetição:
numero = 7
print(f"--- Tabuada do {numero} ---")

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

#Somando valores de uma listaO for também é ótimo para acumular ou somar valores (como notas de alunos ou preços de um carrinho de compras):

notas = [8.5, 7.0, 9.0, 6.5]
soma_total = 0

for nota in notas:
    soma_total = soma_total + nota  # Adiciona a nota atual ao total

print(f"A soma de todas as notas é: {soma_total}")
