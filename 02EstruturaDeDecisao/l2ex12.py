'''12. Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
    Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20%
    Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        - Salário Bruto: (5 * 220)        : R$ 1100,00
        - (-) IR (5%)                     : R$   55,00  
        - (-) INSS ( 10%)                 : R$  110,00
        - FGTS (11%)                      : R$  121,00
        - Total de descontos              : R$  165,00
        - Salário Liquido                 : R$  935,00'''
valor = float(input("Insira o valor da hora de trabalho: R$"))
horas = float(input("Insira a quantidade de horas trabalhadas no mês: "))
salario = valor * horas
if salario > 2500.0:
    ir = salario * 0.20
    percentual = "(20%)"
elif salario <= 2500.0 and salario > 1500:
    ir = salario * 0.10
    percentual = "(10%)"
elif salario <= 1500.0 and salario > 900:
    ir = salario * 0.05
    percentual = "(5%)"
else:
    ir = 0.0
    percentual = "(Isento)"
inss = salario * 0.10
fgts = salario * 0.11
sindicato = salario * 0.03
descontos = ir+inss+sindicato
salario_liq = salario - descontos
print(f'Salário bruto ({horas} * R${valor}): R${salario:.2f}')
print('IR ' + percentual + f': R${ir:.2f}')
print(f'INSS (10%): R${inss:.2f}')
print(f'Sindicato (3%): R${sindicato:.2f}')
print(f'Total de descontos: R${descontos:.2f}')
print(f'FGTS (11%): R${fgts:.2f}')
print(f'Salário líquido é: R${salario_liq:.2f}')