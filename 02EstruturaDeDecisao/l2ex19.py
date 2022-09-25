'''19. Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros.
Exemplo:
    - 326 = 3 centenas, 2 dezenas e 6 unidades
    - 12 = 1 dezena e 2 unidades
Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16'''
num100 = int(input("Insira um número menor que 1000: "))
qtd100 = qtd10 = qtd1 = num10 = 0
#contagem de centenas
if num100//100 > 0:
    qtd100 = num100//100
    num10 = num100 - (qtd100 * 100)
else: 
    num10 = num100
#contagem de dezenas e unidades
if num10//10 > 0:
    qtd10 = num10//10
    qtd1 = num10 - (qtd10 * 10)
else:
    qtd1 = num10
#formatação dos termos no plural
txt100 = txt10 = txt1 = ""
if qtd100 > 1: txt100 = "centenas"
elif qtd100 == 1: txt100 = "centena"
if qtd10 > 1: txt10 = "dezenas"
elif qtd10 == 1: txt10 = "dezena"
if qtd1 > 1: txt1 = "unidades"
elif qtd1 == 1: txt1 = "unidade"
#manipulação da saída
#apenas centenas
if qtd100 > 0 and qtd10 == 0 and qtd1 == 0:
    print(f'{num100} = {qtd100} {txt100}') 
#apenas dezenas
elif qtd100 == 0 and qtd10 > 0 and qtd1 == 0:
    print(f'{num100} = {qtd10} {txt10}')
#apenas unidades
elif qtd100 == 0 and qtd10 == 0 and qtd1 > 0:
    print(f'{num100} = {qtd1} {txt1}')
#centenas e dezenas
elif qtd100 > 0 and qtd10 > 0 and qtd1 == 0:
    print(f'{num100} = {qtd100} {txt100} e {qtd10} {txt10}') 
#centenas e unidades
elif qtd100 > 0 and qtd10 == 0 and qtd1 > 0:
    print(f'{num100} = {qtd100} {txt100} e {qtd1} {txt1}') 
#dezenas e unidades
elif qtd100 == 0 and qtd10 > 0 and qtd1 > 0:
    print(f'{num100} = {qtd10} {txt10} e {qtd1} {txt1}')
#centenas, dezenas e unidades   
else:
    print(f'{num100} = {qtd100} {txt100}, {qtd10} {txt10} e {qtd1} {txt1}')
