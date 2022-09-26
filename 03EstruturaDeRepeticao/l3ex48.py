'''48. Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
    Exemplo:
    12376489
    => 98467321'''
n = input("Insira um número inteiro: ")
start = len(n)-1
for i in range(start,-1,-1):
    print(n[i],end="")