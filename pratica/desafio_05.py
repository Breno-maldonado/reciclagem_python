# Sua missão: Crie uma lista vazia chamada clientes_ativos. Escreva um loop for com if para encontrar os clientes com "ativo" igual a True. Use o .append() para adicionar o nome dos clientes ativos dentro da lista clientes_ativos. No final (fora do loop), dê um print(clientes_ativos).

clientes = [
    {"id": 1, "nome": "Carlos", "ativo": True},
    {"id": 2, "nome": "Mariana", "ativo": False},
    {"id": 3, "nome": "Beatriz", "ativo": True}
]

clientes_ativos = []

for cliente in clientes:
    if cliente["ativo"]:
        clientes_ativos.append(cliente["nome"])

print(clientes_ativos)