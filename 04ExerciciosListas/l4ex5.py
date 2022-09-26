#5. Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
listaInteiros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
listaPar = []
listaImpar = []
for i in listaInteiros:
    if i%2 == 0: listaPar.append(i)
    else: listaImpar.append(i)
print(f'Pares: {listaPar}')
print(f'Ímapres: {listaImpar}')
