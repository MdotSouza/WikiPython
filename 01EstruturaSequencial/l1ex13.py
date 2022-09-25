'''13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
    a. Para homens: (72.7*h) - 58 b. Para mulheres: (62.1*h) - 44.7'''
altura = float(input("Insira a altura em metros: "))
sexo = (input("Insra M para sexo masculino e F para feminino")).upper()
peso = 0.0
if sexo == "M":
    peso = (72.7*altura) - 58
    print(f'O peso ideal para a altura informada é: {peso:.1f} kg')
elif sexo == "F":
    peso = (62.1*altura) - 44.7
    print(f'O peso ideal para a altura informada é: {peso:.1f} kg')
else:
    print("Seleção de sexo incorreta!")