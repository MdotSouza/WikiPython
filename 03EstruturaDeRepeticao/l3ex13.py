#13. Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número.
# Não utilize a função de potência da linguagem.
b = int(input("Insira a base: "))
e = int(input("Insira o expoente: "))
result = 1
for i in range(e):
    result *= b
print(f'Potência = {result}.')
