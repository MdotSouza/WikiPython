'''41. Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
    Os juros e a quantidade de parcelas seguem a tabela abaixo:
    Quantidade de Parcelas      % de Juros sobre o valor inicial da dívida
                1                       0
                3                       10
                6                       15
                9                       20
                12                      25
    Exemplo de saída do programa:
            Valor da Dívida         Valor dos Juros     Quantidade de Parcelas      Valor da Parcela
            R$ 1.000,00             0                   1                           R$  1.000,00
            R$ 1.100,00             100                 3                           R$    366,00
            R$ 1.150,00             150                 6                           R$    191,67'''
valor = float(input("Insira o valor da dívida: R$ "))
print("Valor da Dívida         Valor dos Juros     Quantidade de Parcelas      Valor da Parcela")
print(f'R$ {valor:.2f}               0.0                      1                     {valor:.2f}')
juros = 10.0
for i in range(3,13,3):
    print(f'R$ {valor:.1f}               {valor*(juros/100):.1f}                     {i}                    {(valor+valor*(juros/100))/i:.1f}')
    juros += 5.0
