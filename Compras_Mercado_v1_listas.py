#!/usr/bin/env python3

'''
A finalidade do programa é ótimizar o tempo
no mercado durante as suas compras.
'''

__version__ = "0.1.0"
__author__ = "Emerson Rocha"


# Produtos solicitados aleatóriamente para compra
anotacao = ['Feijão de corda','Tomate','Alface',
'Arroz','Farofa','Refrigerante','Salgadinho','Maçã']

# Definição de setores do Supermercado para alocação dos produtos
mercearia = ['Feijão de corda','Arroz','Farofa']
adega_e_bebidas = ['Refrigerante']
hortifruti = ['Tomate','Alface','Maçã']
bomboniere = ['Salgadinho']


# Aqui foram definidos os alimentos que estão em falta no estoque do Supermercado
produtos_em_falta = [ 
                      (mercearia.remove('Farofa')),
					  ((hortifruti.remove('Maçã')),

)]

#print (produtos_em_falta)


# Definindo a lista de setores para verificação dos suprimentos solicitados
suprimentos = [
			   ('Mercearia', mercearia),
			   ('Adega e Bebidas',adega_e_bebidas),
			   ('Hortifruti', hortifruti),
			   ('bomboniere', bomboniere),
			   
]

print("\n")
print("." * 100)
print("." * 100)
print ("Itens solicitados para compra:\n", anotacao)
print("." * 100)
print("." * 100,"\n")

print(" " * 100,"\n")
print("SETORES E PRODUTOS DISPONÍVEIS")
print(" " * 100)

for nome_suprimento, suprimento in suprimentos:
    print("\n")
    print("*" * 60)
    print(f"Setor de {nome_suprimento}")
    print("*" * 60)
    print("\n")

    suprimento_mercearia = []
    suprimento_adega_e_bebidas = []
    suprimento_hortifruti = []
    suprimento_bomboniere = []    

    for produto in suprimento:
	    if produto in anotacao:
		    suprimento_mercearia.append(produto)
	    elif produto in anotacao:
		    suprimento_adega_e_bebidas.append(produto)
	    elif produto in anotacao:
		    suprimento_hortifruti.append(produto)
	    elif produto in anotacao:
	        suprimento_bomboniere.append(produto)


    print(">", suprimento_mercearia)
    print(">", suprimento_adega_e_bebidas)
    print(">", suprimento_hortifruti)
    print(">", suprimento_bomboniere)