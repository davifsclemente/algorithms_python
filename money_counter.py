# Faça um programa que imprima a menor quantidade
# de cédulas possíveis entre 100, 50, 20, 10, 5, 1.

def menor_cedula(valor):
    nota100 = valor // 100
    nota50 = (valor % 100) // 50
    nota20 = ((valor % 100) % 50) // 20
    nota10 = (((valor % 100) % 50) % 20) // 10
    nota5 = ((((valor % 100) % 50) % 20) % 10) // 5
    nota1 = (((((valor % 100) % 50) % 20) % 10) % 5) // 1

    print('Notas R$100,00 = ', nota100)
    print('Notas R$50,00 = ', nota50)
    print('Notas R$20,00 = ', nota20)
    print('Notas R$10,00 = ', nota10)
    print('Notas R$5,00 = ', nota5)
    print('Notas R$1,00 = ', nota1)


menor_cedula(1469)
