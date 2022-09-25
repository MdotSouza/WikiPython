#6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
from math import pi
r = float(input("Insira a medida do raio: "))
area = pi*(r**2)
print(f'A área do circulo é: {area:.2f}')