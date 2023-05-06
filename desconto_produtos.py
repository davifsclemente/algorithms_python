# Escreva um programa que calcule o valor do desconto de
# uma mercadoria paga à vista e o valor total a ser pago. O
# programa deve ler o valor da mercadoria e a
# porcentagem do desconto. Depois o programa deve
# calcular e imprimir na tela o valor do desconto e o novo
# valor da mercadoria com o desconto.

v_prod = float(input("Informe o preço original do produto: "))
desconto = int(input("Informe o desoconto: "))
total_desconto = v_prod * (desconto / 100)
novo_valor = v_prod - total_desconto

print(f'Valor desocntado: {total_desconto}')
print(f'Novo valor do produto: {novo_valor}')
