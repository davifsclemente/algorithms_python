# Um grupo de amigos pretende alugar um carro por
# um único dia. Consultadas duas agências, a primeira
# cobra R$62,00 pela diária e R$1,40 por quilômetro
# rodado. A segunda cobra diária de R$80,00 e mais
# R$1,20 por quilômetro rodado. Escreva um programa
# que leia a quantidade de quilômetros a serem
# rodados e calcule e imprima na tela o preço a ser
# pago em cada uma das agências.

km_rodados = int(input("Informe a quantidade de quilômetros a serem rodados: "))
ag1 = 0
ag2 = 0
for i in range(0, km_rodados):
    ag1 = i * 1.40
    ag2 = i * 1.20
if ag1 > ag2:
    print(f'Agência 2 é mais econômica.\nValor: {ag2}R$')
else:
    print(f'Agencia 1 é mais econômica.\n Valor: {ag1}R$')
