# Escreva um programa que leia o peso e a altura de
# uma pessoa. Em seguida o programa deve calcular e
# imprimir índice de massa corpórea (IMC) dessa
# pessoa. IMC = peso / (altura)2

peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura: "))
imc = peso / (altura**2)
print(imc)
