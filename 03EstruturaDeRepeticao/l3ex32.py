'''32. Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
    Fatorial de: 5
    5! =  5 . 4 . 3 . 2 . 1 = 120 '''
n = int(input("Insira um número: "))
fatorial = 1
retorno = ""
for i in range (n,0,-1):
    fatorial *= i
    if i != 1: retorno += f'{i} . '
    else: retorno += f'{i} ='
print(f'{n}! = {retorno} {fatorial}')
