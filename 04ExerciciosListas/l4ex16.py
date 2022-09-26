'''16. Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões.
O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana.
Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470.
Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
        - $200 - $299
        - $300 - $399
        - $400 - $499
        - $500 - $599
        - $600 - $699
        - $700 - $799
        - $800 - $899
        - $900 - $999
        - $1000 em diante
Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.'''
listaRanges = [999,899,799,699,599,499,399,299]
listaConts = [0,0,0,0,0,0,0,0]
while True:
    x = float(input("Informe o valor da cenda bruta semanal (-1 para encerrar): R$"))
    if x == -1: break
    else:
        valor = (x*0.09)+200
        pos = 0
        for i in listaRanges:
            if valor > i: listaConts[pos] += 1
            pos += 1
for i in range(len(listaRanges)):
    print(f'{listaRanges[i]} - {listaConts[i]}')
