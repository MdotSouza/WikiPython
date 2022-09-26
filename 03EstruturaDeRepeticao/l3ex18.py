#18. Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
n = int(input("Insira a cardinalidade do conunto (tamanho de elementos): "))
maior = menor = somatorio = 0
for i in range (1,n+1):
    num = int(input(f'Digite o número {i}/{n}: '))
    if i == 1: menor = maior = num
    elif num > maior: maior = num
    elif num < menor: menor = num
    somatorio += num
print(f'MAIOR = {maior}, MENOR = {menor}, soma = {somatorio}')