#7. Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
listaInteriros = [1,2,3,4,5]
multiplicacao = 1
for i in listaInteriros:
    multiplicacao *= i
print(f'Soma: {sum(listaInteriros)}')
print(f'Multiplicação: {multiplicacao}')
