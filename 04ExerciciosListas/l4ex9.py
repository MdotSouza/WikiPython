#9. Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
listaInteiros = [1,2,3,4,5,6,7,8,9,10]
listaQuadrados = []
for i in listaInteiros:
    listaQuadrados.append(i**2)
print(f'Soma dos quadrados = {sum(listaQuadrados)}')
