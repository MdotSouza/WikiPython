#8. Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor.
# Imprima a idade e a altura na ordem inversa a ordem lida.
listaIdades = []
listaAlturas = []
for i in range(1,6):
    idade = int(input(f'Informe a idade da pessoa {i}/5: '))
    altura = float(input(f'Informe a altura da pessoa {i}/5: '))
    listaIdades.append(idade)
    listaAlturas.append(altura)
listaAlturas.reverse()
listaIdades.reverse()
print(listaIdades)
print(listaAlturas)
