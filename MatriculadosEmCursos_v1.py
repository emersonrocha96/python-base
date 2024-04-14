#!/usr/bin/env python3

"""
Exibe relatório de alunos por atividade.

Lista os alunos agrupados por sala que 
frequenta cada uma das atividades.

"""

__version__ = "0.1.0"
__author__ = "Emerson Rocha"


#Sala dos alunos
sala1 = ["Emerson", "Sofia", "João", "Matheus", "Cleber"]
sala2 = ["Fabio", "Marcio","Leandro","Marcelo"]

#Materias estudadas 
aula_ingles = ["Emerson","Sofia", "Cleber","Matheus","Marcelo"]
aula_musica = ["Emerson","João", "Marcio", "Matheus","Sofia"]
aula_danca = ["João", "Matheus", "Sofia","Marcelo"]

# Criando uma lista de todas as matérias
atividades = [
      ( "Inglês", aula_ingles),
      ( "Musica", aula_musica),
      (  "Dança", aula_danca),
 ]


"""
Se o aluno estiver na sala 1, inclua ele 
na na lista da sala_de_ingles1, senão, se
ele estiver na sala 2, inclua ele na lista 
sala_de_ingles2.
"""

# Para o nome_atividade será exibido o label atribuido juntamente com a respectiva
# atividade em cada volta que o laço for executado, por exemplo: A primeira atividade será inglês
for nome_atividade, atividade in atividades:
    print()
    print("-" * 30)
    print(f"Aluno da atividade {nome_atividade}")
    print("-" * 30)
    print()
        
    atividade_sala1 = []
    atividade_sala2 = []

    for aluno in atividade:
    	if aluno in sala1:
    		atividade_sala1.append(aluno)
    	elif aluno in sala2:
    		atividade_sala2.append(aluno)
    		
# Utilizando a interpolação com format para exibir o label recebido seguido da lista de
# alunos inscritos na respectiva atividade.

    print (f"{nome_atividade} Sala 1: ", atividade_sala1)
    print(f"{nome_atividade}  Sala 2: ", atividade_sala2)

# Fazendo um divisor de 30 caracteres para melhorar a saída dos dados
    print ()
    print("#" * 30)
    
