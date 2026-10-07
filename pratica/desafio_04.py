# Sua missão: Escreva um loop for com um if para imprimir o nome apenas dos clientes que estão ativos ("ativo" igual a True).

clientes = [
    {"id": 1, "nome": "Carlos", "ativo": True},
    {"id": 2, "nome": "Mariana", "ativo": False}
]

for cliente in clientes:
    if cliente["ativo"] == True:
        print(cliente["nome"])