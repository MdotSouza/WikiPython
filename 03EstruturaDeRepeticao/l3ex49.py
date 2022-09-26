'''49. Faça um programa que mostre os n termos da Série a seguir:
    - S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
Imprima no final a soma da série. '''
n = int(input("Insira um n-ésimo termo da série: "))
resposta = ""
j = 1
s = 0
for i in range(1,n+1):
    if i == 1 : resposta += f'S = {i}/{j} + '
    elif i < n: resposta += f'{i}/{j} + '
    else: resposta += f'{i}/{j}.'
    j += 2
    s += i/j
print(resposta)
print(s)
