'''28. Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles.
O usuário deverá informar a quantidade de CDs e o valor para em cada um.'''
c = int(input("Insira a quantidade de CDs: "))
somatorio = 0
for i in range(1,c+1):
    valor = float(input(f'Insira a o valor do CD {i}/{c}: R$'))
    somatorio += valor
print(f'Quantidade média de alunos: {somatorio/c:.2f}')
