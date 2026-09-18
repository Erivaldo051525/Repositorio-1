# 1. Crie uma lista vazia chamada notas.

notas = []

# 2. Leia 5 notas e adicione cada uma à lista usando append().
for i in range(5):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)

print("\n ---Resultados---")

# 3. Utilize um for para mostrar todas as notas cadastradas.
print("Notas cadastradas:")
for nota in notas:
    print(nota)

# 4. Mostre a quantidade de notas armazenadas.
print(f"\n Quantidade de notas armazenadas: {len(notas)}")

# 5. Mostre a maior e a menor nota.
print(f"Maior nota: {max(notas)}")
print(f"Menor nota: {min(notas)}")   

"""
media= max(notas)
print(f"media=",media)
if media >=6:
    print("Aluno aprovado")
else:
    print("Aluno reprovado")
"""

media= (max(notas)+min(notas))/2
print(f"media = {media}")
if media <=6:
    print("Aluno aprovado")
else:
    print("Aluno Reprovado")

