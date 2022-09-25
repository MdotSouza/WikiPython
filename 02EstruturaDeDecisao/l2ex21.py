'''21. Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
    - Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
    - Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.'''
valor100 = float(input("Insira valor do saque: "))
valor50 = valor10 = valor5 = 0
notas1 = notas5 = notas10 = notas50 = notas100 = 0
if valor100//100 > 0:
    notas100 = valor100//100
    valor50 = valor100 - (notas100 * 100)
else: 
    valor50 = valor100
if valor50//50 > 0:
    notas50 = valor50//50
    valor10 = valor50 - (notas50 * 50)
else:
    valor10 = valor50
if valor10//10 > 0:
    notas10 = valor10//10
    valor5 = valor10 - (notas10 * 10)
else:
    valor5 = valor10
if valor5//5 > 0:
    notas5 = valor5//5
    notas1 = valor5 - (notas5 * 5)
else:
    notas1 = valor100
print(f'Notas de 100: {int(notas100)}')
print(f'Notas de 50: {int(notas50)}')
print(f'Notas de 10: {int(notas10)}')
print(f'Notas de 5: {int(notas5)}')
print(f'Notas de 1: {int(notas1)}')
