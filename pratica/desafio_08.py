# Sua missão: Crie um dicionário vazio chamado totais_por_status. Percorra a lista transacoes com um loop for. Para cada transação, verifique se o "status" já existe como chave em totais_por_status. Se não existir, inicialize essa chave com 0. Some o "valor" da transação na chave correspondente do status. Imprima o dicionário totais_por_status.

transacoes = [
    {"id": 1, "status": "pago", "valor": 100.0},
    {"id": 2, "status": "pendente", "valor": 250.0},
    {"id": 3, "status": "pago", "valor": 400.0},
    {"id": 4, "status": "cancelado", "valor": 150.0}
]

totais_por_status = {}

for transacao in transacoes:
    status = transacao["status"]
    valor = transacao["valor"]

    if status not in totais_por_status:
        totais_por_status[status] = 0

    totais_por_status[status] += valor

print(totais_por_status)

transacoes = [
    {"id": 1, "status": "pago", "valor": 100.0},
    {"id": 2, "status": "pendente", "valor": 250.0},
    {"id": 3, "status": "pago", "valor": 400.0},
    {"id": 4, "status": "cancelado", "valor": 150.0}
]

total_cancelado = 0

for transacao in transacoes:
    if transacao["status"] == "cancelado":
        total_cancelado += transacao["valor"]

print(total_cancelado)