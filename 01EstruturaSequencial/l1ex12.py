#12. Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
altura = float(input("Insira a altura em metros: "))
peso = (72.7*altura) - 58
print(f'O peso ideal para a altura informada é: {peso:.2f} kg')