# Crie uma lista chamada clientes contendo dois dicionários (dois clientes):
# Primeiro cliente: id: 1, nome: "Carlos", ativo: True
# Segundo cliente: id: 2, nome: "Mariana", ativo: False
# Em seguida, escreva o comando print para mostrar apenas o nome do segundo cliente ("Mariana").

clientes = [
    {"id": 1, "nome": "Carlos", "ativo": True},
    {"id": 2, "nome": "Mariana", "ativo": False}
]

print(clientes[1]["nome"])