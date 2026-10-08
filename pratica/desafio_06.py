# Sua missão: Crie uma variável faturamento_total iniciando em 0. Escreva um loop for para percorrer a lista vendas e somar todos os valores da chave "valor" dentro de faturamento_total. Imprima o resultado final de faturamento_total.

vendas = [
    {"id_venda": 101, "valor": 150.0},
    {"id_venda": 102, "valor": 300.5},
    {"id_venda": 103, "valor": 50.0}
]

faturamento_total = 0

for venda in vendas:
    faturamento_total += venda["valor"]

print(faturamento_total)