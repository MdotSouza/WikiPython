#8. Faça um programa que leia 5 números e informe a soma e a média dos números.
soma = 0.0
for i in range(1,6):
    num = float(input(f"Insira um número {i}/5: "))
    soma += num
print(f'Soma: {soma}. Média: {soma/5:.2f}')
