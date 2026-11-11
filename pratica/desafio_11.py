nome = 'Breno'
idade = 24
print(type(nome), type(idade))

preco1 = 19.99
preco2 = 3
print(type(preco1), type(preco2))

x = 10
y = 3
z = x + y
print(z)

a = 20
b = 4
multiplicacao = a * b
print(multiplicacao)

c = 50
d = 2
divisao = c / d
print(divisao)

num1 = 9
num2 = 2
resto = num1 % num2
print(resto)

notas = [8, 9, 10]
print(notas[1])

tarefas = ['estudar', 'treinar']
tarefas.append('dormir')
print(tarefas)
print(len(tarefas))

convidados = ['Ana', 'Bruno', 'Carlos']
for convidado in convidados:
    print(convidado)

pessoa = {
    'nome': 'Breno',
    'idade': 24,
    'cidade': 'São Paulo'
}
pessoa['idade'] = 25
print(pessoa['idade'])

temperatura = 30
if temperatura >= 25:
    print('Está calor!')
else:
    print('Está fresco!')