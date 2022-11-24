preco = float(input())
qtd = int(input())
valor = preco * qtd
n = qtd * 0.01
a = valor * 0.10
b = valor * n
total = valor - a - b
print(f'{valor:.2f}')
print(f'{total:.2f}')
