#12. Foram anotadas as idades e alturas de 30 alunos.
# Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.
dictIdadesAlturas = {}
for i in range(1,31):
    idade = int(input(f'Insira a idade do aluno {i}/30: '))
    altura = float(input(f'Insira a altura do aluno {i}/30: '))
    dictIdadesAlturas[idade] = altura
media = sum(dictIdadesAlturas.values())/len(dictIdadesAlturas)
cont = 0
for i in dictIdadesAlturas.keys():
    if (i > 13 and dictIdadesAlturas[i] < media): cont += 1
print(cont)
