#24. Faça um programa que calcule o mostre a média aritmética de N notas.
N = int(input("Insira um número: "))
somatorio = 0
for j in range(1,N+1):
    somatorio += j
print(f'Média: {somatorio/N}')