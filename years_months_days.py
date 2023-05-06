# Faça um programa que leia a idade de uma pessoa
# expressa em dias e mostre-a expressa apenas em
# anos, meses e dias. Assuma, neste programa, que um
# ano tem 365 dias e que um mês tem 30 dias.
# Exemplo: Se a pessoa digitar que viveu 10260 dias
# significa que ela tem 28 anos, 1 mês e 10 dias.

dias_vividos = int(input("Quantos dias você viveu? "))
anos = dias_vividos // 365
meses = (dias_vividos % 365) // 30
dias = (dias_vividos % 365) % 30
print(f'Você viveu {anos} anos, {meses} meses e {dias} dias')
