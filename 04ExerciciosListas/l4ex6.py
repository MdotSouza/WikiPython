#6. Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno,
# imprima o número de alunos com média maior ou igual a 7.0.
listaMedias = []
for i in range(1,11):
    listaNotas = []
    for j in range(1,5):
        nota = float(input(f'Inisira a {j}ª nota do aluno {i}/10: '))
        listaNotas.append(nota)
    media = sum(listaNotas)/len(listaNotas)
    listaMedias.append(media)
cont = 0
for i in listaMedias:
    if i >= 7.0:
        cont += 1
print(f'Alunos com média maior ou igual a 7 = {cont}')
