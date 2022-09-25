'''18. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).'''
from math import ceil
tam = float(input("Insira o tamanho do arquivo (em MB): "))
vel = float(input("Insira a velocidade de um link de Internet (em Mbps): "))
duracao = ceil((tam / vel)/60)
print(f'Tempo aproximado de download do arquivo usando este link (em minutos): {duracao}')