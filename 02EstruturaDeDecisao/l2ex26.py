'''26. Um posto está vendendo combustíveis com a seguinte tabela de descontos:
    Álcool:
        - até 20 litros, desconto de 3% por litro
        - acima de 20 litros, desconto de 5% por litro
    Gasolina:
        - até 20 litros, desconto de 4% por litro
        - acima de 20 litros, desconto de 6% por litro
Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível(codificado da seguinte forma: A-álcool, G-gasolina),
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.'''
vol = int(input("Insira quantos litros vendidos: "))
comb = input("Selecione o tipo de combustível (A-álcool, G-gasolina): ").upper()
if comb == "A":
    if vol <= 20: valor = (vol*1.9)*0.97
    else: valor = (vol*1.9)*0.95
    print(f"Valor cobrado: R${valor:.2f}")
elif comb == "G":
    if vol <= 20: valor = (vol*2.5)*0.96
    else: valor = (vol*2.5)*0.94
    print(f"Valor cobrado: R${valor:.2f}")
else:
    print("Seleção incorreta!") 