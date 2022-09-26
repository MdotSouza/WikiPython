'''39. Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros.
Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.'''
alto = baixo = codAlto = codBaixo = 0
for i in range(1,11):
    cod = int(input("Insira o código do aluno: "))
    altura = int(input("Insira a altura do aluno (em cm): "))
    if i == 1:
        alto = baixo = altura
        codAlto = codBaixo = cod
    elif altura > alto:
        alto = altura
        codAlto = cod
    elif altura < baixo:
        baixo = altura
        codBaixo = cod
print(f'Aluno mais alto: {codAlto} / {alto} cm')
print(f'Aluno mais baixo: {codBaixo} / {baixo} cm')
