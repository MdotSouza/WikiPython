#11. Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
lista1 = [1,2,3,4,5,6,7,8,9,10]
lista2 = [-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
lista3 = ['a','b','c','d','e','f','g','h','i','-10']
listaFinal = []
for i in range(len(lista1)):
    listaFinal.append(lista1[i])
    listaFinal.append(lista2[i])
    listaFinal.append(lista3[i])
print(listaFinal)
