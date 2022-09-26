#19. Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
n = int(input("Insira a cardinalidade do conunto (tamanho de elementos): "))
maior = menor = somatorio = 0
for i in range (1,n+1):
    while True:
        num = int(input(f'Digite o número {i}/{n} (apenas valores entre 0 e 1000): '))
        if num >= 0 and num <= 1000: break
    if i == 1: menor = maior = num
    elif num > maior: maior = num
    elif num < menor: menor = num
    somatorio += num
print(f'MAIOR = {maior}, MENOR = {menor}, soma = {somatorio}')
