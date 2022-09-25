'''27. Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                        Até 5 Kg            Acima de 5 Kg
    - Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
    - Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.'''
qtdMorangos = float(input('Insira a quantidade de morangos (em kg): '))
qtdMacas = float(input('Insira a quantidade de maçãs (em kg): '))
valor = 0.0
if qtdMorangos > 5: valor = qtdMorangos*2.2
else: valor = qtdMorangos*2.5
if qtdMacas > 5: valor += qtdMacas*1.5
else: valor += qtdMacas*1.8
if (qtdMacas + qtdMorangos > 8) or valor > 25.0:
    valor *= 0.9
print(f'Valor cobrado: R${valor:.2f}')