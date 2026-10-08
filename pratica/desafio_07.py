# Sua missão: Crie uma variável total_pago iniciando em 0. Escreva um loop for para percorrer as transacoes. Use um if para filtrar apenas as transações cujo "status" seja igual a "pago". Some o "valor" dessas transações na variável total_pago. No final, imprima o valor de total_pago.

transacoes = [
    {"id": 1, "status": "pago", "valor": 100.0},
    {"id": 2, "status": "pendente", "valor": 250.0},
    {"id": 3, "status": "pago", "valor": 400.0},
    {"id": 4, "status": "cancelado", "valor": 150.0}
]

total_pago = 0

for transacao in transacoes:
    if transacao["status"] == "pago":
        total_pago += transacao["valor"]

print(total_pago)