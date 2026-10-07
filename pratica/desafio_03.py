# Sua missão: Escreva um loop for que percorra a lista clientes e imprima apenas o nome de cada cliente.

clientes = [
    {"id": 1, "nome": "Carlos", "ativo": True},
    {"id": 2, "nome": "Mariana", "ativo": False}
]

for lista in clientes:
    print(lista["nome"])