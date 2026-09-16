nome = str(input("Digite seu nome: "))

print ("== Menu de defeitos ==")
print ("1 - sistema indisponivel")
print ("2 - sistema funcionando, mas com lentidão ou erros")
print ("3 - problema que não impede o trabalho")
print ("4 - outros problemas")

opcao = int(input("Com a ajuda do menu, digite o numero que representa seu problema:  "))
tempo = int(input("Digite a quantas horas o problema está ocorrendo: "))

if opcao == 1:
    problema = "sistema indisponivel"
    prioridade = "critica"

elif opcao == 2:
    problema = "sistema funcionando, mas com lentidão"
    prioridade = "alta"

elif opcao == 3: 
    problema = "problema que não impede o trabalho"
    prioridade = "media"

elif opcao == 4: 
    problema = "outros problemas"
    prioridade = "baixa" 

else:
    problema = "opção invalida"
    prioridade = "não definida"


print("=== CHAMADO DE SUPORTE ---")
print ("usuario: ", nome)
print ("problema: ", problema)
print ("tempo: ", tempo, "hora(s)")
print ("prioridade: ", prioridade)



