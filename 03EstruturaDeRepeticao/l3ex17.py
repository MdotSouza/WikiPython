#17. Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
n = int(input("Insira um número: "))
fatorial = n
for i in range (n-1,1,-1):
    fatorial *= i
print(f'{n}! = {fatorial}')
