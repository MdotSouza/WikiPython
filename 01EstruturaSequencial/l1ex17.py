'''17. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00. Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    - comprar apenas latas de 18 litros;
    - comprar apenas galões de 3,6 litros;
    - misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é,
    considere latas cheias.'''
from math import ceil, floor
area = (float(input("Insira o tamanho da área pintada em m²: ")))*1.1
cob_lata = 18.0*6 #cobertura em m² de uma lata
cob_galao = 3.6*6 #cobertura em m² de um galão
#situação 1: apenas latas
latas = ceil(area / cob_lata)
custo1 = latas * 80.0
#situação 2: apenas galões
galoes = ceil(area / cob_galao)
custo2 = galoes * 25.0
#situação 3: latas e galões
latas2 = floor((area / cob_lata))
area_sobra = area - (cob_lata * latas2)
galoes2 = 0
if latas2 == 0.0:
    latas2 = latas
elif area_sobra > 0.0:
    galoes2 = ceil(area_sobra/cob_galao)
custo3 = latas2 * 80.0 + galoes2 * 25.0   
#resultados    
print(f'Opção de venda 1. Latas: {latas} un. Custo R${custo1:.2f}')
print(f'Opção de venda 2. Galões: {galoes} un. Custo R${custo2:.2f}')
print(f'Opção de venda 3. Latas: {latas2} un. Galões: {galoes2} un. Custo R${custo3:.2f}')