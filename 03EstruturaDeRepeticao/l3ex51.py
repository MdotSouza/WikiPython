'''51. Faça um programa que mostre os n termos da Série a seguir:
    S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
    Imprima no final a soma da série. '''
n = int(input("Insira um n-ésimo termo da série: "))
h = 0
retorno = ""
for i in range(1,n+1):
    h += 1/i
    if i == 1:
        retorno += f'= 1/{i} + '
    elif  i == n:
        retorno += f' 1/{i} ='
    else:
        retorno += f' 1/{i} +'
print(f'H {retorno} {h:.2f}')