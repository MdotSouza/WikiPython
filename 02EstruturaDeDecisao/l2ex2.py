#2. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
num = int(input("Insira um número: "))
if num > 0:
    print(f'O valor é POSITIVO')
elif num < 0:
    print(f'O valor é NEGATIVO')
else:
    print(f'O valor é NULO')
