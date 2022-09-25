'''16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.'''
area = float(input("Insira o tamanho da área pintada em m²: "))
latas = area / (18*3)
if latas//1 != latas:
    latas = int(latas+1)
custo = latas * 80.0
print(f'A quantidade de latas necessárias é: {latas:.2f}. O custo é: R${custo:.2f}')
