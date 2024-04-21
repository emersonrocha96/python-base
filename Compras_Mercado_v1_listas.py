#!/usr/bin/env python3

'''
A finalidade do programa é ótimizar o tempo
no mercado durante as suas compras.
'''

__version__ = "0.1.0"
__author__ = "Emerson Rocha"


# Produtos solicitados aleatóriamente para compra
anotacao = ["Feijão de corda","Tomate","Alface",
"Arroz","Farofa","Refrigerante","Salgadinho","Maçã"]



# Definição de setores do Supermercado para alocação dos produtos
mercearia = ["Feijão de corda","Arroz","Farofa"]
adega_e_bebidas = ["Refrigerante"]
hortifruti = ["Tomate","","Maçã"]
bomboniere = ["Salgadinho"]

# Definição de informação para quando não exitir o produto solicitado
vazio = "Sem Estoque" 
 

# Definindo a lista de setores para verificação dos suprimentos solicitados
suprimentos = [
			   ("Mercearia", mercearia),
			   ("Adega e Bebidas",adega_e_bebidas),
			   ("Hortifruti", hortifruti),
			   ("bomboniere", bomboniere),
]

for nome_suprimento, suprimento in suprimentos:

	print("-" * 30)
	print(f"Setor de {nome_suprimento}\n")

	suprimento_mercearia = []
	suprimento_adega_e_bebidas = []
	suprimento_hortifruti = []
	suprimento_bomboniere = []
	sem_estoque = []

	for produto in suprimento:
		if produto in anotacao:
			suprimento_mercearia.append(produto)
		elif produto in anotacao:
			suprimento_adega_e_bebidas.append(produto)
		elif produto in anotacao:
			suprimento_hortifruti.append(produto)
		elif produto in anotacao:
			suprimento_bomboniere.append(produto)
		
	print("Produto:", suprimento)

