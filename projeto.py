#Calculamento de média 2.0
#Autor: Matheus Henrique
#09/10/2025
print("Seja bem-vindo(a)")
print("Chamada dos alunos")
add = str(input("Adicione o nome do aluno:"))
nota = float(input("Coloque os números de faltas:"))
nota2 = float(input("Coloque nota da prova:"))
nota3 = float(input("Nota de participação:"))
nota4 = float(input("Atividades feitas (vistos):"))
nota5 = float(input("Pontos tirados (-):"))
soma = nota + nota2 + nota3 + nota4 
menos = soma - nota5 
conta = menos / 4

print(f"O {add} ficou com {conta} de média. ")
