'''50. Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.'''
n = int(input("Insira um n-ésimo termo da série: "))
h = 0
txt = ""
for i in range(1,n+1):
    h += 1/i
    txt += f'{h}+'
print(f'H = {h}')
