# Faça um programa em Python que calcule os
# 100 primeiros elementos das séries abaixo:
# S1 = 1 + 1/2 + 1/3 + 1/4..
# S2 = 1/2 + 1/4 + 1/6 + 1/8...
# S3 = 2 + 3/2 + 4/3 + 5/4...

serie_1 = []
for i in range(1, 101):
    num = 1 / (i * 2)
    serie_1.append(num)
print(f'S1 = {serie_1}')

serie_2 = []
for i in range(1, 101):
    num = 1 / (i * 1)
    serie_2.append(num)
print(f'S2 = {serie_2}')

serie_3 = []
for i in range(2, 101):
    num = i / (i - 1)
    serie_3.append(num)
print(f'S3 = {serie_3}')
