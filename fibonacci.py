# Sequência de Fibonacci
n = int(input("Informe o valor pra gerar a sequência: "))
n1 = 1
n2 = 1
for i in range(2, n):
    fibo = n1 + n2
    n2 = n1
    n1 = fibo
    print(fibo)
