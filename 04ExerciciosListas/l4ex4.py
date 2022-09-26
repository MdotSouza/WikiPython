#4. Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes
listaCaracteres = ['a','b','c','d','e','f','g','h','i','j']
cont = 0
listaConsoantes = []
for i in listaCaracteres:
    if (i.lower() in 'aeiou') == False:
        cont += 1
        listaConsoantes.append(i)
print(f'Consoantes {cont}. {listaConsoantes}')
