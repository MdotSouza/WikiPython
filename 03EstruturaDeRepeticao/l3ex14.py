#14. Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.
par = impar = 0
for i in range(1,11):
    num = int(input(f"Insira o número {i}/10: "))
    if num%2 == 0: par += 1
    else: impar += 1
print(f'Números pares {par}. Números ímpares {impar}.')
