#23. Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.
num = float(input("Insira um número inteiro ou decimal: "))
if num//1 == num: print("O número informado é inteiro.")
else: print("O número informado é decimal.")
