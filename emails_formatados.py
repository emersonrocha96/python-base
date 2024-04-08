#!/usr/bin/env python3

email = """

Olá, %(nome)s

Somos da %(empresa)s e gostariamos de saber você teria interesse
em adiquirir o nosso produto %(produto)s ?

Com ele você poderar manter %(texto)s

Temos apenas %(qtd)d disponiveis, valor promocional de %(preco).2f

Acesse já o nosso site %(link)s e garanta sua vaga!
"""

clientes = ["Marcos","Felipe", "Emerson", "Maria", "Rafaela", "Jéssica"]

for cliente in clientes:
    print(
        email %{
        "nome": cliente,
        "empresa": "Rocha Seguros 96",
        "produto": "Seguro Veicular Premium",
        "texto": """Seu(s) veiculo(s) protegidos 24 horas,
         gps, alarme e carro reserva""",
        "qtd": 5,
        "preco": 250.0,
        "link": "rochaseguros.com",
         }
    )
