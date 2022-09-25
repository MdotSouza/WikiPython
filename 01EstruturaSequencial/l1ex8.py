#8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
valor = float(input("Insira o valor da hora de trabalho: "))
horas = float(input("Insira a quantidade de horas trabalhadas no mês: "))
print(f'O total do salário será R$: {valor*horas:.2f}')