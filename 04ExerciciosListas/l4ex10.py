'''10. Faça um Programa que leia dois vetores com 10 elementos cada.
Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.'''
lista1 = [1,2,3,4,5,6,7,8,9,10]
lista2 = [-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
listaFinal = []
for i in range(len(lista1)):
    listaFinal.append(lista1[i])
    listaFinal.append(lista2[i])
print(listaFinal)
