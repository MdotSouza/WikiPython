#7. Faça um programa que leia 5 números e informe o maior número.
maior = 0.0
for i in range(1,6):
    num = float(input(f"Insira um número {i}/5: "))
    if num > maior: maior = num
print(f'O maior número digitado foi: {maior}.')
