'''42. Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100].
A entrada de dados deverá terminar quando for lido um número negativo.'''
int1 = int2 = int3 = int4 = 0
while True:
    n = int(input("Insira um número entre 0 e 100 (digite qualquer número negativo para encerrar): "))
    if n < 0: break
    elif n >= 0 and n <= 25: int1 += 1 #intervalo [0-25]
    elif n >= 26 and n <= 50: int2 += 1 #intervalo [26-50]
    elif n >= 51 and n <= 75: int3 += 1 #intervalo [51-75]
    elif n >= 76 and n <= 100: int4 += 1 #intervalo [76-100]
print(f'''Números no intervalo [0-25] = {int1}
Números no intervalo [26-50] = {int2}
Números no intervalo [51-75] = {int3}
Números no intervalo [76-100] = {int4}''')
